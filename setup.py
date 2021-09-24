#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore
from setuptools.command.sdist import sdist
from shutil import which
from subprocess import check_call


class EnsureBundlesThenInstall(sdist):
   def run(self):
       if which("node") is None:
           raise ValueError("Install node to create an sdist.")
       print('Building JavaScript...')
       check_call(['npm', 'install', '--silent', '--cwd', 'js'])
       check_call(['npm', 'run', 'build', '--quiet', '--cwd', 'js'])
       sdist.run(self)


with open("README.md") as readme_file:
    readme = readme_file.read()


setup(
    author="Observable, Inc.",
    author_email="support@observablehq.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Embed Observable cells hosted on observablehq.com into Jupyter notebooks.",
    install_requires=[],
    license="ISC license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="observable_jupyter",
    name="observable_jupyter",
    packages=find_packages(include=["observable_jupyter", "observable_jupyter.*"]),
    cmdclass={'sdist': EnsureBundlesThenInstall},
    setup_requires=[],
    extras_require={
        'test': [
            'pytest',
            'IPython'
        ],
        'dev': [
            'jupyter',
            'nox',
            'pytest',
        ]
    },
    url="https://github.com/observablehq/observable_jupyter",
    version="0.1.7",
    zip_safe=False,
)
