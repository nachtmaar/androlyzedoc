# setup.py
import os,glob
from setuptools import setup,find_packages

setup(
    name = "androlyze",
    author = "Nils Schmidt",
    author_email = "schmidt89 at informatik.uni-marburg.de",
    license = "MIT",

    packages=find_packages('androlyze'),
    package_dir = {'':'androlyze'},

    include_package_data = True,

    scripts=['androlyze/androlyze.py'],

   install_requires=[
        "pymongo",
        "celery",
        "ipython",
        "networkx",
        "boto",
        "fabric",
        "simplejson",
        "numpydoc",
],
)
