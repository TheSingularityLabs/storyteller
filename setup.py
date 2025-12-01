"""Setup configuration for Storyteller framework"""
from setuptools import setup, find_packages

setup(
    name="storyteller",
    version="1.0.0",
    description="A Python framework for parsing explainer video scripts, managing layout patterns, and orchestrating video creation workflows",
    packages=find_packages(exclude=['tests', 'tests.*']),
    python_requires=">=3.8",
    install_requires=[],
)

