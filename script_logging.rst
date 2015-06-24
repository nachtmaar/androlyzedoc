Logging
=======

AndroLyzeLab comes with a built-in logging object which is directly connected to MongoDB.
Internally the logging object is represented as an :py:mod:`collections.OrderedDict`.

Before you can use it, you have to register the basic structure.
This is intended for better comparison of the results afterwards.

If you try to log to some key that hasn't been registered an exception will be raised.
Therefore you should test your script locally before you run it on a cluster!

During the script development you should use the the static function :py:meth:`.AndroScript.test` to test if your script runs correctly.

There are three different keys that you can register and/or log to:

* bool: Registers a boolean key. Will be set to False

* enum: Register an enumeration key. Will create a list internally which can be used to append iterative.

* normal: Will register None as default. You can log any `JSON Serializable data <https://docs.python.org/2/library/json.html#json.JSONEncoder>`_.


Demo
----

The logging is pretty self-explenatory. So we don't have to spend much time here. Just have a look at the logging of this very simple script and the produced output:

.. literalinclude:: ../androlyze/model/script/impl/ShowLoggingFuncs.py

There are a few things to notice. First there is a static and a dynamic part of the result. The categories "apk meta" and "script meta" are part of every result.
The dynamic part is the data you log.
Second it shows the result layout before and after logging values to it.
The layout after registering the basic layout can be seen at ("category", "category2", "unlogged"). The final result after logging some values to it at ("category", "category2", "logged").

.. code-block:: sh

	{
		"apk meta": {
			"package name": "com.myfitnesspal.android",
			"version name": "3.7.3",
			"sha256": "4d2afc03880795a561e8eb762314d135d7a777d50daa72fafbcb64b1cbb7ae4d",
			"import date": "2015-06-20T20:07:49.775000",
			"build_date": "2015-02-09T07:47:10",
			"path": "/home/worker/androlyze/apks/02.03.2015_top_free_4/apps_topselling_free/HEALTH_AND_FITNESS/com.myfitnesspal.android.apk",
			"tag": null
		},
		"script meta": {
			"name": "ShowLoggingFuncs",
			"sha256": "2331b99382b960948d38c7ba85789ca903c02d0e42ddda7603138d413c78e889",
			"analysis date": "2015-06-21T19:26:40.158000",
			"version": "0.1"
		},
		"category1": {
			"category2": {
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
		}
	}


The fact that you need to register a structure doesn't mean you can't log to dynamic keys.
It just means you have to register the key before you try to log to it!


Common mistakes
---------------

* Forgetting to unpack tuple for category usage!

	.. code-block:: sh
	 
		res.log("key", "value", ("foo", "bar"))

instead of

	.. code-block:: sh
	 
		res.log("key", "value", *("foo", "bar"))


Using different output formats
------------------------------

You don't have to use the built-it :py:class:`.ResultObject` for logging.
You can also supply your custom log object and specify a custom file name extension.

Just have a look at the following example.

.. literalinclude:: ../androlyze/model/script/impl/GVMAnalysisExample.py


