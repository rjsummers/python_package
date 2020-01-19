import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-rjsummers",
    version="0.0.1",
    author="Randall Summers",
    author_email="rsummers@ou.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/rjsummers/python_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # See https://pypi.org/classifiers/
    python_requires='>=3.6',
)
