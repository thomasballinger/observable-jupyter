#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore
from setuptools.command.sdist import sdist
from setuptools.command.install import install
from setuptools.command.develop import develop
from shutil import which
from subprocess import check_call
import re

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    open('observable_jupyter/__init__.py', encoding='utf_8_sig').read()
).group(1)


def build_js():
    if which("node") is None:
        raise ValueError("Install node to create an sdist.")
    check_call(['npm', 'install', '--silent', '--prefix', 'js'])
    check_call(['npm', 'run', 'build', '--quiet', '--prefix', 'js'])

class BuildJsAndSdist(sdist):
    def run(self):
        print('Building JavaScript as part of sdist...')
        build_js()
        sdist.run(self)

class BuildJSAndInstall(install):
    def run(self):
        print('Building JavaScript as part of install...')
        build_js()
        install.run(self)

class BuildJSAndDevelop(develop):
    def run(self):
        print('Building JavaScript as part of develop...')
        build_js()
        develop.run(self)


with open("README.md") as readme_file:
    readme = readme_file.read()


setup(
    author="Thomas Ballinger",
    author_email="me@ballingt.com",
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
    cmdclass={
        'sdist': BuildJsAndSdist,
        'install': BuildJSAndInstall,
        'develop': BuildJSAndDevelop,
    },
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
    version=__version__,
    zip_safe=False,
)
