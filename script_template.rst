Script Template
===============

Use the following as a template to write your custom script.

The basics steps for writing a custom scripts are:

* rename the script class (has to be the same name as the module!)
* change the :py:meth:`.AndroScript._analyze` method to reflect your custom analysis
* define the script requirements needed (by default everything is disabled allowing only to access the basic :py:class:`.Apk` class)

Optional:

* use a custom logging object (e.g. to store the data to a file)
* save the results in MongoDBs gridFS if they may exceed 16MB

.. note::

	There is a utility class for disassembling, decompiling, accessing the abstract syntrax tree etc.
	Have a look at :py:mod:`.AnaUtil`

This is the template:

.. literalinclude:: androlyze/androlyze/model/script/ScriptTemplate.py

