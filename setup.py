from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fizzbuzzco",
    version="0.0.3",
    description="FizzBuzz For Corporate Practices",
    py_modules=["FizzBuzz"],
    package_dir={"": "src"},

    classifier=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Langauge :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/Si-ja/FizzBuzz-Co..git",
    author="Si_ja",
    author_email="none@none.none"
)