#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Thomas Ballinger",
    author_email="ballingt@observablehq.com",
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
    package_data={"observable_jupyter_embed": ["py.typed"]},
    include_package_data=True,
    keywords="observable_jupyter_embed",
    name="observable_jupyter_embed",
    package_dir={"": "src"},
    packages=find_packages(
        include=["src/observable_jupyter_embed", "src/observable_jupyter_embed.*"]
    ),
    setup_requires=[],
    url="https://github.com/thomasballinger/observable_jupyter_embed",
    version="0.1.0",
    zip_safe=False,
)
