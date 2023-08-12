"""
Setup for package
"""

from setuptools import setup, find_packages

setup(
    name="assetBuilder",
    version='0.1.1',
    description="Command line tools for generating ironsworn assets",
    author='Itay Ben Haim',
    packages=find_packages(include=['asset_builder', 'asset_builder.*']),
    install_requires=[
        "click==8.1.6",
        "colorama==0.4.6",
        "html2image==2.0.3",
        "Markdown==3.4.4",
        "yattag==1.15.1"
    ],
    entry_points={
        "console_scripts": ["assetBuilder=asset_builder.main:cli"]
    },
)
