#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

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
    setup_requires=[],
    url="https://github.com/observablehq/observable_jupyter",
    version="0.1.7",
    zip_safe=False,
)
