import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "my_package",
    version = "0.0.1",
    author = "terminal based snake game",
    author_email = "narasyimmha@gmail.com",
    description = ("README.md"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "https://github.com/NarasyimmhaUmapathy/sriraracha_snake",
    packages=['spicy_snake'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)