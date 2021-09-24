import nox  # type: ignore
from pathlib import Path

nox.options.sessions = ["tests"]

python = ["3.6", "3.7", "3.8", "3.9"]


@nox.session(python=python)
def tests(session):
    session.install("-e", ".[test]", )
    tests = session.posargs or ["tests"]
    session.run(
        "pytest",
        *tests
    )


@nox.session(python="3.9")
def js_tests(session):
    session.run("npm", "--cwd", "js", "install", external=True)
    session.run("npm", "--cwd", "js", "test", external=True)


@nox.session(python="3.9")
def edit_example(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "Jupyter")
    session.run("Jupyter", "notebook", "Observable_Embed_Example.ipynb")


@nox.session(python="3.9")
def jupyter_notebook_test(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "jupyter")
    session.run("jupyter", "notebook", "test_notebook.ipynb")

@nox.session(python="3.9")
def jupyter_lab_test(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "jupyterlab")
    session.run("jupyter", "lab", "test_notebook.ipynb")

@nox.session()
def build(session):
    session.install("setuptools")
    session.install("wheel")
    session.install("twine")
    session.run("rm", "-rf", "dist", "build", external=True)
    session.run("python", "setup.py", "--quiet", "sdist", "bdist_wheel")

@nox.session(python="3.7")
def publish(session):
    build(session)
    print("REMINDER: Has the changelog been updated?")
    session.run("python", "-m", "twine", "upload", "dist/*")
