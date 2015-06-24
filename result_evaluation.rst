
Result evaluation
=================

In the same way you can write a script you can also define how to perform queries against the result database.
Have a look at the `Eval` class of the script template.

The class enables a direct way to the API of the MongoDB driver as well as the simplified query API from `AndroLyze`.

The script can be evaluated by running

.. code-block:: sh

    ./androeval androlyze/model/script/ScriptTemplate.py


.. literalinclude:: ../androlyze/model/script/ScriptTemplate.py

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