import nox  # type: ignore
from pathlib import Path

nox.options.sessions = ["tests"]

python = ["3.7", "3.8", "3.9", "3.10"]

@nox.session(python="3.10")
def tests(session):
    session.install("-e", ".[test]", )
    tests = session.posargs or ["tests"]
    session.run(
        "pytest",
        *tests
    )

@nox.session(python=python)
def tests_on_all_versions(session):
    session.install("-e", ".[test]", )
    tests = session.posargs or ["tests"]
    session.run(
        "pytest",
        *tests
    )

@nox.session(python="3.10")
def js_tests(session):
    session.run("npm", "--prefix", "js", "--silent", "install", external=True)
    session.run("npm", "--prefix", "js", "test", external=True)

@nox.session(python="3.10")
def edit_example(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "Jupyter")
    session.run("Jupyter", "notebook", "Observable_Embed_Example.ipynb")

@nox.session(python="3.10")
def jupyter_notebook_manual_test(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "jupyter")
    session.run("jupyter", "notebook", "test_notebook.ipynb")

@nox.session(python="3.10")
def jupyter_lab_manual_test(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "jupyterlab")
    session.run("jupyter", "lab", "test_notebook.ipynb")

# there's not c extension, so we don't need a separate build per Python version!
@nox.session(python="3.10")
def build(session):
    session.install("setuptools")
    session.install("wheel")
    session.install("twine")
    session.run("rm", "-rf", "dist", "build", external=True)
    session.run("python", "setup.py", "--quiet", "sdist", "bdist_wheel")

@nox.session(python="3.10")
def docs(session):
    session.install("-r", "docs/requirements.txt")
    with session.cd("docs"):
        session.run('make', 'html')


@nox.session(python="3.10")
def publish(session):
    build(session)
    print("REMINDER: Has the changelog been updated?")
    session.run("python", "-m", "twine", "upload", "dist/*")
