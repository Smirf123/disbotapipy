import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Smirf123", # Replace with your own username
    version="1.0.0",
    author="Smirf123",
    author_email="matthewelert@gmail.com",
    description="A simple api wrapper for the Disbot.top API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smirf123/disbotapipy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
