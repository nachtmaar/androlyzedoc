AndroLyze
============

:Release: |version|
:Date: |today|

About
-----
AndroLyze is a distributed framework for android app analysis with unified logging and reporting functionality to perform security checks on large numbers of applications in an efficient manner.

It provides optimized scheduling algorithms for distributing static code analysis tasks across several machines. Moreover, it can handle several versions of a single mobile application to generate a security track record over many versions.

The code and documentation is related to the following paper (link will follow):

.. image:: https://raw.githubusercontent.com/nachtmaar/androlyzedoc/master/gfx/androlyze_paper.png
	:width: 90%
	:align: center

Features
--------
- Static android code analysis based on `Androguard <https://github.com/androguard/androguard>`_
- Unified logging and reporting framework backed by `mongoDB <https://www.mongodb.com>`_
- Efficient Android app analysis on a single machine | local cluster | cloud
- APK distribution via mongoDB, Amazon S3 or serialization of the local .apk files
- Code-Size Scheduling: Schedule long running tasks first based on the size of the `classes.dex` file
- Download APKs from `Google play <https://play.google.com/store>`_ with the help of `Google Play Crawler <https://github.com/Akdeniz/google-play-crawler>`_
- Update your APK collection by downloading the newest APK version to create a security track record over several versions

Try it out!
-----------
Still interested? Try it out!
We provide an easy way to install *AndroLyze* using `Docker <https://www.docker.com>`_ containers.

License
-------
`AndroLyze` is licensed under the `MIT <https://tldrlegal.com/license/mit-license>`_ license.

Documentation
-------------

The documentation is hosted at `readthedocs.org <https://androlyze.readthedocs.org>`_ and opensource available at `github <https://github.com/nachtmaar/androlyzedoc>`_. Feel free to contribute!
Edit the docs on github, commit it and it will be automatically built by readthedocs!

.. toctree::
    :maxdepth: 2
    :hidden:

    install
    usage
    scripts
    scripts_demo
    getting_apks
    monitoring

.. autoclass:: apidoc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


