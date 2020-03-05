__all__ = ["embed"]

import json
from typing import List, Dict

try:
    from IPython.display import display, HTML
except ImportError:
    print("Expected a Jupyter environment.")
    raise


def embed(
    slug: str, cell_names: List[str] = None, inputs: Dict = None, use_iframe=True
) -> None:
    """Embeds a set of cells or an entire Observable notebook.
    """

    if inputs is None:
        inputs = {}

    # TODO: check formatting on slug, allow full url?
    # TODO: do the global state checks (or the mutation observers?) to detect that we're re-running this.
    # TODO: run in iframe
    # TODO: include default Observable styles when an iframe is used?

    if cell_names and set(cell_names) & set(inputs):
        raise ValueError("specify cell names as output or input, not both")

    jsonified_inputs = jsonify(inputs)

    # a JavaScript expression that evaluates to true for cells that should be rendered
    if cell_names is None:
        filter_code = f"true"
    else:
        assert all(isinstance(name, str) and name.isidentifier() for name in cell_names)
        filter_code = f'({" || ".join(cell_names)})'

    html = f"""<div id="observablehq-883ab4d6"></div>
<script type="module">
const inputs = {jsonified_inputs}
import {{Runtime, Inspector}} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/{slug}.js?v=3";
const inspect = Inspector.into("#observablehq-883ab4d6");
const main = (new Runtime).module(define, name => {filter_code} && inspect());
for (let name of Object.keys(inputs)) {{
  main.redefine(name, inputs[name]);
}}
</script>

"""

    if not use_iframe:
        display(HTML(html))
    else:
        raise NotImplementedError()


def jsonify(obj):
    return json.dumps(obj, cls=DataJSONEncoder)


class DataJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "DataFrame":  # Pandas DataFrame
            return json.dumps(obj.to_dict(orient="records"))
