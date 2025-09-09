from setuptools import setup, find_packages

setup(
    name="cbda",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "flask>=2.3.0",
        "streamlit>=1.22.0",
    ],
    entry_points={
        "console_scripts": [
            "cbda-api=src.realtime_analysis.api:main",
            "cbda-dashboard=src.dashboard.app:main",
        ]
    },
)
