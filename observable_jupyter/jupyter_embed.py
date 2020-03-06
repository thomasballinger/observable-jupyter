__all__ = ["embed"]


import json
import random
import pkg_resources
from typing import List, Dict

iframe_bundle_fname = pkg_resources.resource_filename(
    "observable_jupyter", "iframe_bundle.js"
)
wrapper_bundle_fname = pkg_resources.resource_filename(
    "observable_jupyter", "iframe_bundle.js"
)

try:
    from IPython.display import display, HTML
except ImportError:
    print("Expected a Jupyter environment.")
    raise


def embed(
    slug: str, cells: List[str] = None, inputs: Dict = None, use_iframe=True
) -> None:
    """Embeds a set of cells or an entire Observable notebook.
    """
    if cells and inputs and set(cells) & set(inputs):
        raise ValueError(
            f"specify cell names as output or input, not both: {set(cells) & set(inputs)}"
        )

    jsonified_inputs = jsonify(inputs or {})

    # a JavaScript expression that evaluates to true for cells that should be rendered
    if cells is None:
        filter_code = f"true"
    else:
        assert all(isinstance(name, str) and name.isidentifier() for name in cells)
        filter_code = (
            f"""({" || ".join(f'name === "{cell_name}"' for cell_name in cells)})"""
        )

    # TODO: stop using generated div ID, it makes notebook output unstable
    iframe_id = f"observable-embed-div-{str(random.random())[2:]}"

    html = f"""<div id="{iframe_id}"></div>
<script type="module">
const inputs = {jsonified_inputs}
import {{Runtime, Inspector}} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/{slug}.js?v=3";
const inspect = Inspector.into("#{iframe_id}");
const main = (new Runtime).module(define, name => {filter_code} && inspect());
for (let name of Object.keys(inputs)) {{
  main.redefine(name, inputs[name]);
}}
</script>"""

    iframe_bundle_src = open(iframe_bundle_fname).read()
    if "`" in iframe_bundle_src:
        raise ValueError("Whoops, no backticks in JavaScript bundle pls")

    iframe_src = f"""<!DOCTYPE html>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">
<script>
{iframe_bundle_src}
</script>
{html}
<script>
ObservableJupyter.monitor("{iframe_id}")
</script>
"""

    # To sidestep the (apparently buggy?) parsing that Jupyter does
    # of script tags in template string, add the script tags in JavaScript.
    iframe_src_script_escaped = iframe_src.replace("<script>", "OPENSCRIPT").replace(
        "</script>", "CLOSESCRIPT"
    )
    iframe_wrapper = f"""<iframe id="{iframe_id}" sandbox="allow-scripts" style="overflow: auto;" frameBorder="0"></iframe>
<script>
iframeSrc = `{iframe_src_script_escaped}`.replace(/OPENSCRIPT/gi, '<sc' + 'ript>').replace(/CLOSESCRIPT/gi, '</sc' + 'ript>')
document.getElementById('{iframe_id}').srcdoc = iframeSrc;

(() => {{
  function onMessage(msg) {{
    console.log('got message', msg.data);
    if (msg.data.type === 'iframeSize') {{
      var el = document.getElementById('{iframe_id}');
      if (el) {{
        console.log('setting dimensions of', el.id, 'to', msg.data.width, msg.data.height);
        el.width = msg.data.width;
        el.height = msg.data.height;
      }} else {{
        removeEventListener('message', onMessage);
      }}
    }}
  }};

  window.addEventListener('message', onMessage);
}})();
</script>
    """

    if use_iframe:
        display(HTML(iframe_wrapper))
    else:
        display(HTML(html))


def jsonify(obj):
    return json.dumps(obj, cls=DataJSONEncoder)


class DataJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "DataFrame":  # Pandas DataFrame
            return json.dumps(obj.to_dict(orient="records"))
