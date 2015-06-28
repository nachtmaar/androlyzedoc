
Result evaluation
=================

In the same way you can write a script you can also define how to perform queries against the result database.
Have a look at the `Eval` class of the script template.

The class enables a direct way to the API of the MongoDB driver as well as the simplified query API from `AndroLyze`.

But be sure you have ran it before:

.. code-block:: sh

  worker@ee6ff2ae704e:/home/worker/androlyze$ ./androanalyze androlyze/model/script/ScriptTemplate.py --apks apks/
  INFO: appending "androguard/" to sys.path
  Welcome to AndroLyze!

  Loaded scripts:
  ScriptTemplate 0.1
  WARNING: Analyzed 1 apks
  done
  WARNING: Took 0:00:01 (h/m/s)

The script can be evaluated by running:

.. code-block:: sh

  worker@ee6ff2ae704e:/home/worker/androlyze$ ./androeval androlyze/model/script/ScriptTemplate.py
  INFO: appending "androguard/" to sys.path
  evaluating 'ScriptTemplate' version: 0.1
  {u'_id': u'5d3e57fdbea31b2f0f1fa0e30b6df866d7b25b60bda3a6ccfd77f0490fa36c12',
   u'apk meta': OrderedDict([(u'package name', u'de.uni_marburg.ipcinetcallee'), (u'version name', u'1.0'), (u'sha256', u'2289f4ec4d4c753e920f7841a5f329ecc6abec3d2865b85bb9a55467cb056877'), (u'import date', None), (u'build_date', datetime.datetime(2015, 4, 21, 19, 35, 56)), (u'path', None), (u'tag', None)])}
  WARNING: Took 0:00:00 (h/m/s)

The result shows the query performed in :py:meth:`.ScriptTemplate._evaluate` directly using the mongodb driver and shows an equivalent query using `AndroLyze`.

.. literalinclude:: androlyze/model/script/ScriptTemplate.py

Manual
------

.. code-block:: sh

    worker@06f5e795c279:/home/worker/androlyze$ ./androeval -h
    INFO: appending "androguard/" to sys.path
    usage: androeval [-h] [-idb IMPORT_DATABASE] [-rdb RESULT_DATABASE_NAME]
                     [-c CONFIG] [-q] [-v] [-vl VLOG] [-V] [--yes]
                     [scripts [scripts ...]]

    positional arguments:
      scripts               Scripts for the db analysis

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Load a custom config file [default: conf/config.conf].
      -V, --version         show program's version number and exit
      --yes, -y             Autoconfirm question(s) on the command-line interface.

    database:
      -idb IMPORT_DATABASE, --import-database IMPORT_DATABASE
                            You can supply a custom import database [default:
                            conf/config.conf]
      -rdb RESULT_DATABASE_NAME, --result-database-name RESULT_DATABASE_NAME
                            You can supply a custom result database name.
                            [default: conf/config.conf]

    logging:
      -q, --quiet           Be quiet and do not log anything to stdout
      -v, --verbose         Set verbosity [default: 3], 1 -> CRITICAL, 2 -> ERROR,
                            3 -> WARN, 4 -> INFO, 5 -> DEBUG
      -vl VLOG, --verbose-log VLOG
                            Log stdout and stderr to file