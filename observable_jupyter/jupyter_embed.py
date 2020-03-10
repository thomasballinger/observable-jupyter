__all__ = ["embed"]


import json
import random
import html
import html.entities as entities
import pkg_resources
from typing import List, Dict

iframe_bundle_fname = pkg_resources.resource_filename(
    "observable_jupyter", "iframe_bundle.js"
)
iframe_bundle_src = open(iframe_bundle_fname).read()
wrapper_bundle_fname = pkg_resources.resource_filename(
    "observable_jupyter", "wrapper_bundle.js"
)
wrapper_bundle_src = open(wrapper_bundle_fname).read()

escapes = {v: k for k, v in entities.html5.items()}


def escape(s):
    """Escape template string syntax."""
    return s.replace("\\", r"\\").replace("`", r"\`").replace("$", r"\$")


try:
    from IPython.display import display, HTML
except ImportError:
    print("Expected a Jupyter environment.")
    raise


def embed(slug: str, cells: List[str] = None, inputs: Dict = None,) -> None:
    """Embeds a set of cells or an entire Observable notebook.
    """
    if cells and inputs and set(cells) & set(inputs):
        raise ValueError(
            f"specify cell names as output or input, not both: {set(cells) & set(inputs)}"
        )

    jsonified_inputs = jsonify(inputs or {})

    if cells:
        for cell in cells:
            if not isinstance(cell, str):
                raise ValueError("Cell names should be strings.")

    # Brackets in Python f-strings are escaped by using two brackets: { -> {{, } -> }}
    iframe_src = f"""<!DOCTYPE html>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">
<style>
body {{
  margin: 0;
}}
</style>
<script>
{iframe_bundle_src}
</script>
<div style="overflow: auto;"></div>
<script type="module">
const inputs = {jsonified_inputs};
const slug = '{slug}';
const into = document.getElementsByTagName('div')[0];
const cells = {repr(cells) if cells else "undefined"}
const main = ObservableJupyterIframe.embed(slug, into, cells, inputs);
ObservableJupyterIframe.monitor(main)
</script>
"""

    iframe_id = f"observable-embed-div-{str(random.random())[2:]}"

    # To sidestep the (apparently buggy?) parsing that Jupyter does
    # of script tags in template strings, add the script tags in JavaScript.
    iframe_src_script_escaped = escape(
        iframe_src.replace("<script>", "OPENSCRIPT").replace("</script>", "CLOSESCRIPT")
    )
    iframe_wrapper = f"""<iframe id="{iframe_id}" sandbox="allow-scripts" style="overflow: auto; min-width: 100%; width: 0px;" frameBorder="0"></iframe>
<script>
{wrapper_bundle_src}
</script>
<script>
iframeSrc = `{iframe_src_script_escaped}`.replace(/OPENSCRIPT/gi, '<sc' + 'ript>').replace(/CLOSESCRIPT/gi, '</sc' + 'ript>')
document.getElementById('{iframe_id}').srcdoc = iframeSrc;
ObservableJupyterWrapper.listenToSize(document.getElementById('{iframe_id}'));
</script>
    """

    display(HTML(iframe_wrapper))


def jsonify(obj):
    return json.dumps(obj, cls=DataJSONEncoder)


class DataJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "DataFrame":  # Pandas DataFrame
            return json.dumps(obj.to_dict(orient="records"))
