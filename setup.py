from setuptools import setup, find_packages

setup(
    name="PyObjectNotation",
    version="1.0.0",
    author="DevLimeGames",
    author_email="dev.limegames@gmail.com",
    description="PYON is a simple text-based format for storing structured data. This module allows loading and saving PYON files, converting them into Python dictionaries and vice versa.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devlimegames/pyon",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    license="Creative Commons Attribution-NonCommercial 4.0 International",
    python_requires=">=3.6",
)