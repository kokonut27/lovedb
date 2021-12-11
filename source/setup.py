from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "lovedb",
  version = "0.0.1",
  description = "A database easily syntaxed for easy use.",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "",
  author = "JBYT27",
  author_email = "beol0127@gmail.com",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT License",
  packages=['lovedb'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)