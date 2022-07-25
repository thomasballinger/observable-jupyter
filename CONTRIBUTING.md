Clone the repo on GitHub and clone it so you have a copy on your local machine.

Make sure you have Python 3.10 installed.
Make sure you have Node.js installed.

OPTIONAL: create a virtual environment and activate it.

Install project automation tool [`nox`](https://nox.thea.codes/en/stable/):
This runs commands in new virtualenvironments.

```
python -m pip install nox
```

### Unit Tests

```
nox -s tests
nox -s js_tests
nox -s jupyter_notebook_manual_test
nox -s jupyter_lab_manual_test
```

### Publish to PyPI

```
nox -s publish
```

