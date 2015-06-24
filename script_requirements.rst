Script requirements
===================

For performance issues, you need to define which features your script needs.

The :py:class:`.Analyzer` checks the minimum requirements to run all supplied scripts.
You can see it at the beginning of the analysis if you set the logging level to info (via the -vvvv switch).

The more features a script requires, the longer it will take.

Currently, there are 5 possible ones:

* :py:meth:`.AndroScript.needs_dalvik_vm_format`

* :py:meth:`.AndroScript.needs_vmanalysis`

* :py:meth:`.AndroScript.needs_gvmanalysis`

* :py:meth:`.AndroScript.needs_xref`

* :py:meth:`.AndroScript.needs_dref`

Have a look at the links to get further information or simply test wether you need them (:py:meth:`.AndroScript.test`).

.. Another thing you should keep in mind, is that :py:class:`.AndroScript` implements the :py:class:`.Resetable` interface.
.. This means all initialisation code you need to set up your script should be moved into the :py:meth:`AndroScript.reset` method.

.. Because your script will not be initialisied for every new apk. Instead only the :py:meth:`AndroScript.reset` will be called.
