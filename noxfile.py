import nox  # type: ignore
from pathlib import Path

nox.options.sessions = ["tests", "lint", "build"]

python = ["3.6", "3.7", "3.8"]


lint_dependencies = [
    "-e",
    ".",
    "black",
    "flake8",
    "flake8-bugbear",
    "mypy",
]


@nox.session(python=python)
def tests(session):
    session.install("-e", ".", "pytest", "pytest-cov", "IPython")
    tests = session.posargs or ["tests"]
    session.run(
        "pytest",
        "--cov=observable_jupyter",
        "--cov-config",
        ".coveragerc",
        "--cov-report=",
        *tests
    )
    session.notify("cover")


@nox.session()
def js_tests(session):
    session.run("yarn", "--cwd", "js")
    session.run("yarn", "--cwd", "js", "test", external=True)


@nox.session(python="3.7")
def edit_example(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "Jupyter")
    session.run("Jupyter", "notebook", "example.ipynb")


@nox.session(python="3.7")
def jupyter_test(session):
    """Open the example Jupyter notebook with a dev install of this module"""
    session.install("-e", ".", "Jupyter")
    session.run("Jupyter", "notebook", "test_notebook.ipynb")


@nox.session
def cover(session):
    """Coverage analysis"""
    session.install("coverage")
    session.run("coverage", "report", "--show-missing", "--fail-under=0")
    session.run("coverage", "erase")


@nox.session(python="3.7")
def lint(session):
    session.install(*lint_dependencies)
    files = ["tests"] + [str(p) for p in Path(".").glob("*.py")]
    session.run("black", "--check", *files)
    session.run("flake8", *files)
    session.run("mypy", *files)
    session.run("python", "setup.py", "check", "--metadata", "--strict")


@nox.session(python="3.7")
def build(session):
    session.install("setuptools")
    session.install("wheel")
    session.install("twine")
    session.run("rm", "-rf", "dist", "build", external=True)
    session.run("yarn", "--cwd", "js")
    session.run("yarn", "--cwd", "js", "build", external=True)
    session.run("python", "setup.py", "--quiet", "sdist", "bdist_wheel")


@nox.session(python="3.7")
def publish(session):
    build(session)
    print("REMINDER: Has the changelog been updated?")
    session.run("python", "-m", "twine", "upload", "dist/*")
