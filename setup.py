import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="persona-api",
    version="0.0.1",
    author="Jonathan Henson",
    author_email="jonathan@henson.me.uk",
    description="A fake RESTful API that delivers made up data on a few endpoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.9',
)