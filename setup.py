from setuptools import setup, find_packages

setup(
    name="cnnClassifier",
    version="0.0.1",
    author="Sayan",
    author_email="sayan@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)