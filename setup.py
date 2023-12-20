from setuptools import setup, find_packages

setup(
    name="snowfl",
    version="0.1.0",
    description="A Python package that allows users to search for content on Snowfl, apply sorting, and filter NSFW content, returning results as an array of objects with relevant information.",
    author="chocotonic",
    author_email="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "certifi==2023.11.17",
        "charset-normalizer==3.3.2",
        "idna==3.6",
        "requests==2.31.0",
        "urllib3==2.1.0",
    ],
)
