__all__ = ["embed"]

import json
import random
from typing import List, Dict

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
    div_id = f"observable-embed-div-{str(random.random())[2:]}"

    html = f"""<div id="{div_id}"></div>
<script type="module">
const inputs = {jsonified_inputs}
import {{Runtime, Inspector}} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/{slug}.js?v=3";
const inspect = Inspector.into("#{div_id}");
const main = (new Runtime).module(define, name => {filter_code} && inspect());
for (let name of Object.keys(inputs)) {{
  main.redefine(name, inputs[name]);
}}
</script>"""

    iframe_src = f"""<!DOCTYPE html>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@observablehq/inspector@3/dist/inspector.css">
{html}"""

    # To sidestep the parsing that Jupyter does of script tags,
    # tack on the script tag in JavaScript.
    assert iframe_src.endswith("</script>")
    iframe_wrapper = f"""<iframe id="{div_id}" sandbox="allow-scripts" style="resize: both; overflow: auto;"></iframe>
<script>
iframeSrc = `{iframe_src[:-3]}` + 'pt>';
document.getElementById('{div_id}').srcdoc = iframeSrc
</script>
    """

    if not use_iframe:
        display(HTML(html))
    else:
        display(HTML(iframe_wrapper))


def jsonify(obj):
    return json.dumps(obj, cls=DataJSONEncoder)


class DataJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "DataFrame":  # Pandas DataFrame
            return json.dumps(obj.to_dict(orient="records"))
