"""Setup configuration for Storyteller framework"""
from setuptools import setup, find_packages

setup(
    name="storyteller",
    version="1.0.0",
    description="A Python framework for parsing explainer video scripts, managing layout patterns, and orchestrating video creation workflows",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies required for core framework
    ],
)

