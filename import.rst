Import
======

At first, we create an import database so that we can easily manage our APKs. Importing is not necessary, but enables an improved scheduling which is based on the size of the dex code.

.. code-block:: sh


    # Import APKs and copy them to the distributed APK storage (mongoDB or Amazon S3 atm.)
    # This enables us to send only the id of APK and fetch if from the storage via network
    ./androimport -cdb apks/

    # Copy the APKs to the result dir defined in the config sorted by package name, hash and version name
    ./androimport -cd apks/

    # Do both
    ./androimport -cd -cdb apks/

    # Use a custom import database
    ./androimport -idb dbs/foo.db -cdb apks/

Manual
------

.. code-block:: sh

    worker@cf0c3ee3e7ca:/home/worker/androlyze$ ./androimport --help
    INFO: appending "androguard/" to sys.path
    usage: androimport [-h] [-idb IMPORT_DATABASE] [-rdb RESULT_DATABASE_NAME]
                       [-c CONFIG] [-q] [-v] [-vl VLOG] [-V] [--yes] [-cd] [-cdb]
                       [-t TAG] [-u] [--concurrency CONCURRENCY]
                       apks [apks ...]

    positional arguments:
      apks                  The apk files or directories (with .apk files). Apk
                            files and directories can also be mixed.

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Load a custom config file [default: conf/config.conf].
      -V, --version         show program's version number and exit
      --yes, -y             Autoconfirm question(s) on the command-line interface.
      -t TAG, --tag TAG     Tag the apks
      -u, --update          Update already imported apks
      --concurrency CONCURRENCY
                            Number of processes

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

    apk copying:
      -cd, --copy-disk      Import the .apk file(s) to the storage dir defined in
                            the config file.
      -cdb, --copy-db       Import the .apk file(s) into the database. Optional
                            for the distributed analysis!