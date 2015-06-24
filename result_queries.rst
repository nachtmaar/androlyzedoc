Querying MongoDB
================

Sample Queries
--------------

Filtering
~~~~~~~~~

There are many other options for filtering. Simply have a look at 
it:

.. code-block:: sh

	./androquery result -h

All commands are run with "-l", showing only the latest result.
So your command-line doesn't get flooded!

For writing advanced queries with mongoDB: `See available Operators <http://docs.mongodb.org/manual/reference/operator/>`_.

To check how AndroLyzeLab formulates the queries use the "-vvvvv" switch.


Here are a few examples:

.. code-block:: sh

	# filerting via script name
	./androquery result -sn ApkInfo -l
	
	# via package name
	./androquery result -pn a2dp.Vol -l

	# both
	./androquery result -pn a2dp.Vol -sn ApkInfo -l	

Filter booleans, lists and not set values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lets take this as an example for the following queries:

.. code-block:: json

	{
	    "apk meta": {
	        "package name": "a3g.emyshoppinglist", 
	        "version name": "2.3.3", 
	        "sha256": "dc7838b0fd5fef035cf8a1d3f4a3244297e64758e432038e9d0525eb41274453", 
	        "import date": "2014-05-05T19:06:18.994000", 
	        "path": "testenv/apks/a3g.emyshoppinglist.apk", 
	        "tag": null
	    }, 
	    "script meta": {
	        "name": "ShowLoggingFuncs", 
	        "sha256": "e9266c885ee44345f5bb5c20fd5f6cd42e05c5061ebff6ae3ebb1cd66678f8a2", 
	        "analysis date": "2014-05-05T20:34:19.006000", 
	        "version": "0.1"
	    }, 
	    "logged": {
	        "normal": "some value", 
	        "bool": true, 
	        "enum": [
	            "list element"
	        ]
	    }, 
	    "unlogged": {
	        "normal": null, 
	        "bool": false, 
	        "enum": []
	    }
	}

.. code-block:: sh

	# filter by logged.enum == []
	./androquery result -sn "ShowLoggingFuncs" --checks-empty-list "logged.enum" -l

	# filter by logged.enum != []
	./androquery result -sn "ShowLoggingFuncs" --checks-non-empty-list "logged.enum" -l

	# logged.enum != [] and logged.bool = True
	./androquery -vvvvv -c testenv.conf result -sn "ShowLoggingFuncs" --checks-non-empty-list logged.enum --checks-true logged.bool --conjunction and -l

	# logged.enum != [] or logged.bool = True
	./androquery -vvvvv -c testenv.conf result -sn "ShowLoggingFuncs" --checks-non-empty-list logged.enum --checks-true logged.bool --conjunction or -l

Fully customized for your need
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

	# custom where filtering
	./androquery result --where "apk meta.package name" a2dp.Vol "script meta.name" Files -l

	# same result with full customized where filtering
	./androquery result --where-dict '{"apk meta.package name" : "a2dp.Vol", "script meta.name" : "Files"}' -l

Projection
~~~~~~~~~~

The following examples are based on the Activities script.
So first have a look at some example result:

(data retrivied via ./androquery  result -sn Activities -l)

.. code-block:: json
	
	{
	    "activities": {
	        "all": [
	            "activision.mw3lwp.PromoActivity", 
	            "activision.mw3lwp.TestActivity", 
	            "activision.mw3lwp.WallpaperSettings"
	        ], 
	        "main activity": "activision.mw3lwp.PromoActivity"
	    }, 
	    "apk meta": {
	        "version name": "1.0", 
	        "package name": "activision.mw3lwp", 
	        "tag": null, 
	        "path": "/Users/nils/Dropbox/AndroLyzeLab/testenv/apks/activision.mw3lwp.apk", 
	        "import date": "2014-04-30T21:32:49.451000", 
	        "sha256": "b14ba7bc6ab38f4d786bd61fdc8b589186bf52cb0b954ebf4b75c1a8a43b14af"
	    }, 
	    "script meta": {
	        "version": "0.1", 
	        "sha256": "6812c8cbb59a0ccc531f7cbdf442202e0c5e73a4493498a21087be182863ba12", 
	        "name": "Activities", 
	        "analysis date": "2014-05-01T10:05:40.532000"
	    }
	}

Examples:

.. code-block:: sh

	# project on attribute "script meta.analysis date", "script meta.name"
	./androquery result -sn Activities -pn a2dp.Vol -if "script meta.analysis date" "script meta.name"

.. code-block:: json


	{
	    "script meta": {
	        "analysis date": "2014-04-30T21:44:03.220000", 
	        "name": "Activities"
	    }
	}

.. code-block:: sh

	# project on attribute activities, apk meta
	./androquery result -sn Activities -pn a2dp.Vol -if "activities" "apk meta"

	# this is the same as excluding script meta
	./androquery result -sn Activities -pn a2dp.Vol -ef "script meta"

Result:

.. code-block:: json

	{
	    "activities": {
	        "all": [
	            "a2dp.Vol.AppChooser", 
	            "a2dp.Vol.CustomIntentMaker", 
	            "a2dp.Vol.EditDevice", 
	            "a2dp.Vol.ListViewer", 
	            "a2dp.Vol.ManageData", 
	            "a2dp.Vol.Preferences", 
	            "a2dp.Vol.ProviderList", 
	            "a2dp.Vol.main"
	        ], 
	        "main activity": "a2dp.Vol.main"
	    }, 
	    "apk meta": {
	        "version name": "2.5.2", 
	        "package name": "a2dp.Vol", 
	        "tag": null, 
	        "path": "/Users/nils/Dropbox/AndroLyzeLab/testenv/apks/a2dp.Vol.apk", 
	        "import date": "2014-04-30T21:32:48.264000", 
	        "sha256": "8805f9028002831a3409537901d42f5ad3cca280fabe6cdc42bfcdd4e9ddbb90"
	    }
	}


Non-documents
~~~~~~~~~~~~~

You can store large data in `mongoDB's gridfs <http://docs.mongodb.org/manual/core/gridfs/>`_ (files > 16mb).
The data is encoded as binary and split into multiple chunks.

To signalize AndroLyzeLab, that you query gridfs instead of the normal document collection, specifiy  "-nd" or "--non-document" !

Doing this results in getting the metadata for the binary data.
If you want to retrieve the binary data, also supply  "-r" or "--raw"!

One :py:class:`.AndroScript` that stores it's data in gridfs, is :py:class:`.GVMAnalysisExample`.


.. code-block:: sh

	# will not return any results! "-nd" not supplied!
	./androquery  result -sn GVMAnalysisExample -l

	# but this will return the metadata
	./androquery  result -sn GVMAnalysisExample -nd -l

	# and this the raw data
	./androquery  result -sn GVMAnalysisExample -nd -r -l

	# count stored results in gridfs
	./androquery  result -nd --count

	# get latest meta infos in gridfs (sort by analysis date, descending)
	./androquery  result -nd -l

	# get latest raw in gridfs (sort by analysis date, descending)
	./androquery  result -nd -r -l

Other options
~~~~~~~~~~~~~

.. code-block:: sh
	
	# sort by analysis date (descending) -> last results firsts
	# also limit results
	./androquery  result -sn Activities -s --limit 2

	# show _id field
	./androquery  result -sn Activities -si -if _id -l

.. code-block:: json

	{
	    "_id": "53621c748d8aee578d1d59f2"
	}


Distinct values
~~~~~~~~~~~~~~~~

.. code-block:: sh
	
	# get script which ran for package name
	./androquery result -pn a2dp.Vol -lrs

.. code-block:: sh

	Activities
	AnalyzeFrameworks
	ApkInfo
	BroadcastReceivers
	Libs
	All
	ChainedApkInfos
	ClassDetails
	ClassListing
	ContentProviders
	Disassembly
	Files
	Intents
	Permissions
	Services

.. code-block:: sh
	
	# get script which ran for package name stored in gridfs
	./androquery result -nd -lrs

.. code-block:: sh
	
	# get script hashes which ran of package name
	./androquery result -pn a2dp.Vol -d "script meta.sha256"


Delete
------

.. code-block:: sh

	# delete all entries for script ChainedApkInfos
	./androdelete  result -sn ChainedApkInfos

	# delete all entries for script ChainedApkInfos with version 0.1
	./androdelete  result -sn ChainedApkInfos -sv 0.1

	# with package name a2dp.Vol
	./androdelete  result -pn a2dp.Vol

	# delete whole result database, will ask for confirmation!
	./androdelete -vvvvv  result --all


Key escaping
------------
When searching for keys you have to keep some things in mind.
Keys are not allowed to begin with "$" and may not contain "." .
AndrolyzeLab escapes the first appeareance of "$" with "_$"
and replaces all "." in a key  with "_".

If you need to automate your queries, you can use the following functions:

.. doctest::

	>>> # key replacement
	>>> from androlyzelab.storage.resultdb.MongoUtil import escape_key, escape_keys
	>>> key = "foo.bar.foo"
	>>> d = {key : []}

.. doctest::
	
	>>> print escape_key(key)
	foo_.bar_.foo

.. doctest::

	>>> print escape_keys(d)
	{'foo_.bar_.foo': []}