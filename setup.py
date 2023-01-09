from setuptools import find_packages, setup

requirements = open("requirements.txt").read().strip().split("\n")

setup(
    name="pdfmerger",
    version=1.0,
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pdfmerger=pdfmerger.app:main"]},
    install_requires=requirements,
)
