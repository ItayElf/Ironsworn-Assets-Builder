"""
Setup for package
"""

from setuptools import setup, find_packages

setup(
    name="assetBuilder",
    version="0.2.0",
    description="Command line tools for generating ironsworn assets",
    author="Itay Ben Haim",
    packages=find_packages(include=["asset_builder", "asset_builder.*"]),
    author="Itay Ben Haim",
    packages=find_packages(include=["asset_builder", "asset_builder.*"]),
    install_requires=[
        "certifi==2024.2.2",
        "chardet==5.2.0",
        "charset-normalizer==3.3.2",
        "certifi==2024.2.2",
        "chardet==5.2.0",
        "charset-normalizer==3.3.2",
        "click==8.1.6",
        "colorama==0.4.6",
        "html2image==2.0.4.3",
        "idna==3.6",
        "html2image==2.0.4.3",
        "idna==3.6",
        "Markdown==3.4.4",
        "pillow==10.2.0",
        "PyYAML==6.0.1",
        "reportlab==4.1.0",
        "requests==2.31.0",
        "urllib3==2.2.1",
        "watchdog==4.0.0",
        "websocket-client==1.7.0",
        "yattag==1.15.1"
    ],
    entry_points={
        "console_scripts": ["assetBuilder=asset_builder.main:cli"]
    },
)
