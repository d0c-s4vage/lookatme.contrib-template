"""
Setup for {{cookiecutter.project_name}}
"""


from setuptools import setup, find_namespace_packages
import os


setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.0",
    description="{{cookiecutter.description}}",
    author="",
    author_email="",
    python_requires=">=3.5",
    packages=find_namespace_packages(include=["lookatme.*"]),
)
