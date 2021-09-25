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
logo_fname = pkg_resources.resource_filename("observable_jupyter", "logo.svg")
logo_src = open(logo_fname).read()


escapes = {v: k for k, v in entities.html5.items()}


def escape(s):
    """Escape template string syntax."""
    return s.replace("\\", r"\\").replace("`", r"\`").replace("$", r"\$")


try:
    from IPython.display import display, HTML
except ImportError:
    print("Expected a Jupyter environment.")
    raise


def embed(
    slug: str, cells: List[str] = None, inputs: Dict = None, display_logo=True
) -> None:
    """Embeds a set of cells or an entire Observable notebook.
    """
    if cells and inputs and set(cells) & set(inputs):
        raise ValueError(
            f"specify cell names as output or input, not both: {set(cells) & set(inputs)}"
        )

    if slug.startswith("http"):
        raise ValueError("notebook identifier looks like a url, please path a specifier like @observablehq/a-taste-of-observable or d/4575c6c14b706a4f")

    jsonified_inputs = jsonify(inputs or {})

    pretty_slug = "embedded notebook" if slug.startswith("d/") else slug

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
ObservableJupyterIframe.embed(slug, into, cells, inputs).then(m => {{window.main = m;}});
ObservableJupyterIframe.monitor()
window.addEventListener('unload', () => {{
  if (typeof window.main !== 'undefined') {{
      window.main._runtime.dispose();
  }}
}});
</script>
"""
    link_back = (
        f"""
<style>
.observable-logo {{
  position: absolute;
  bottom: 0;
  right: 0;
  margin-bottom: 5px;
  margin-right: 1px;
  transition: background-color 0.2s;
}}
.observable-logo svg {{
  opacity: 0.5;
  transition: opacity 0.2s;
}}
.observable-logo span {{
  opacity: 0;
  transition: opacity 0.2s;
  padding-right: .2em;
  padding-left: .2em;
}}
.observable-logo:hover {{
  background-color: white;
}}
.observable-logo:hover span {{
  opacity: .8;
}}
.observable-logo:hover svg {{
  opacity: .8;
}}
.observable-link:hover ~ iframe {{
  outline: solid 1px #E0E0E0;
  box-shadow: 0 0 3px;
  transition: box-shadow 0.2s;
}}
.observable-link ~ iframe {{
    outline: none;
}}
/* Colab-only rule - untested */
body > .output-area > .output-body {{
  margin-right: 2px;
}}
</style>
<a class="observable-link" href="https://observablehq.com/{slug}" target="_blank" style="text-decoration: none; color: inherit;">
<div class="observable-logo" style="display: flex; align-items: center; justify-content: flex-end;">
<span>Edit {pretty_slug} on Observable</span>
{logo_src}
</div>
</a>
"""
        if display_logo
        else ""
    )

    iframe_id = f"observable-embed-div-{str(random.random())[2:]}"

    # To sidestep the (apparently buggy?) parsing that Jupyter does
    # of script tags in template strings, add the script tags in JavaScript.
    iframe_src_script_escaped = escape(
        iframe_src.replace("<script>", "OPENSCRIPT").replace("</script>", "CLOSESCRIPT")
    )
    iframe_wrapper = f"""<div style="text-align: right; position: relative">
    {link_back}
    <iframe id="{iframe_id}" sandbox="allow-scripts" style="overflow: auto; min-width: 100%; width: 0px;" frameBorder="0"></iframe>
</div>
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
