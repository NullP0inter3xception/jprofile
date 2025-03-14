from setuptools import setup, find_packages

setup(
    name="jprofile",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    author="NullP0inter3xception",
    description="A simple Python library for data profiling of pandas DataFrames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NullP0inter3xception/jprofile",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)