from setuptools import setup, find_packages
import codecs
import os

VERSION = '1'
DESCRIPTION = 'Prime Number'
LONG_DESCRIPTION = 'A package for defining prime number.'

# Setting up
setup(
    name="prime_number",
    version=VERSION,
    author="SaminMustakim",
    author_email="saminshamima@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['math'],
    keywords=['prime', 'math', 'mathematics', 'python tutorial', 'samin mustakim', 'prime number'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)