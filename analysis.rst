
Analysis
========

The following section shows by example how to trigger the analysis process and how to view the results.
All built-in scripts are located in the `scripts_builtin` folder. User written scripts can be placed in `scripts_user`.

Decompile
---------

We start by decompiling the APKs (which we previously imported) with androguard's DAD decompiler.
A batch job analyzes one APK after another parallel on all available cores.

.. code-block:: sh

    ./androanalyze scripts_builtin/DecompileClassesText.py -pm parallel
    INFO: appending "androguard/" to sys.path
    Welcome to AndroLyze!

    Using Code Size Scheduling for faster analysis!
    Loaded scripts:
    DecompileClassesText 0.1
    => [2/101 (1.98 %) | 0:09:30 | com.infraware.office.link 6.0.9]


Because the DecompileClassesText may exceed 16MB - the maximum size of mongoDB documents - the source code is stored binary.
This is signaled by the "-nd" switch

.. code-block:: sh

    $ ./androquery result -sn DecompileClassesText -nd

    {
        "chunkSize": 261120,
        "filename": "com.ebay.mobile_2.8.2.1_DecompileClassesText.java",
        "length": 25931939,
        "uploadDate": "2015-06-20T20:46:43.703000",
        "md5": "521bbd5e9ec78a263ddabbd60f921e45",
        "metadata": {
            "decompiled_classes": null,
            "apk meta": {
                "build_date": "2014-11-12T09:57:38",
                "version name": "2.8.2.1",
                "package name": "com.ebay.mobile",
                "tag": null,
                "path": "/home/worker/androlyze/apks/02.03.2015_top_free_4/apps_topselling_free/SHOPPING/com.ebay.mobile.apk",
                "import date": "2015-06-17T17:43:16.024000",
                "sha256": "9e6bf1cb31f5cff3a3d8e39a16ca8c34590ad68ae840b4bb7995f185af0f0994"
            },
            "script meta": {
                "version": "0.1",
                "sha256": "c52a19607c2db12034d409bf3e15546d10199d724a939a63a9699ad0daa14f3f",
                "name": "DecompileClassesText",
                "analysis date": "2015-06-20T20:38:54.705000"
            }
        }
    }

MongoDB stores binary files in two collections. One contains the meta information, the other the binary chunks. The last command only showed the meta data.
To view the actual content, one has to append the "-r" or "--raw" switch.
The following command stores the disassembly of the ebay application in a text file called "com.ebay.mobile.java".

.. code-block:: sh


     ./androquery result -sn DecompileClassesText -nd -r -pn com.ebay.mobile > com.ebay.mobile.java


Code Permissions
----------------

The `CodePermissions` scripts checks where the app uses which permissions and lists the locations in the code as well as the decompiled code using them.
This time we don't perform the analysis local. Instead we use the distributed system of `AndroLyze` signaled with the "-pm distributed
switch. The default parallelization mode can be customized in the config file. 

If the APKs have been imported to MongoDB or Amazon S3 one should use the "-si" switch so that only the hashes of the APKs are send.

The following command insteads serializes the APKs and includes them in the message, stored in the distributed task queue:

.. code-block:: sh

    worker@06f5e795c279:/home/worker/androlyze$ ./androanalyze scripts_builtin/CodePermissions.py -pm distributed
    INFO: appending "androguard/" to sys.path
    Welcome to AndroLyze!

    Using Code Size Scheduling for faster analysis!
    Loaded scripts:
    CodePermissions 0.1
    Will serialize .apk data!
    Registered workers: celery@06f5e795c279
    Number of apks to analyze: 101
    Task publishing progress:
    Send tasks: 101, current task id: 5c9f66e7-678d-4d7e-a252-79f44938a303, queue: analyze_apk
    Analysis progress:
    Successful: 100, Failed: 0, Total: 100/101 (99.01 %) -- Time elapsed: 0:49:08
    analysis done ...
    Successful: 101, Failed: 0, Total: 101/101 (100.00 %) -- Time elapsed: 0:49:09
    WARNING: Analyzed 101 apks
    done
    WARNING: Took 0:49:10 (h/m/s)

The result can be queried like this:

.. code-block:: sh

    {
        "apk meta": {
            "package name": "com.ebay.mobile",
            "version name": "2.8.2.1",
            "sha256": "9e6bf1cb31f5cff3a3d8e39a16ca8c34590ad68ae840b4bb7995f185af0f0994",
            "import date": "2015-06-20T20:08:07.745000",
            "build_date": "2014-11-12T09:57:38",
            "path": "/home/worker/androlyze/apks/02.03.2015_top_free_4/apps_topselling_free/SHOPPING/com.ebay.mobile.apk",
            "tag": null
        },
        "script meta": {
            "name": "CodePermissions",
            "sha256": "9fae70af3c3ec7693a1f454d67633442da7d5173aab304b25f04be49f6459e47",
            "analysis date": "2015-06-21T15:59:23.837000",
            "version": "0.1"
        },
        "code permissions": {
            "listing": {
                "ACCESS_NETWORK_STATE": [
                    "Lcom.ebay.mobile.notifications.PushService$LogNotificationRequest.buildXmlRequest",
                    "Lcom.ebay.common.net.api.cal.LogMessage$LogMessageClientDetails.createLogMessageClientDetail",
                    "Lcom.google.android.gms.internal.ec.<init>",
                    "LRLSDK.a.a",
                    "Lcom.ebay.nautilus.kernel.net.Connector.getConnectedNetworkInfo",
                    "Lcom.ebay.mobile.analytics.mts.MtsAnalyticsAdapter.getNetworkType",
                    "Lcom.paypal.android.lib.riskcomponent.RiskComponent.getRefreshedRiskBlob",
                    "Lcom.google.android.gms.internal.ec.a"
                ],
                "NFC": [
                    "Lcom.ebay.mobile.NfcCompat.isBeamPushEnabled"
                ],
            },
            ...
        "code": {
            "ACCESS_NETWORK_STATE": [
                {
                    "Lcom_ebay_mobile_analytics_mts_MtsAnalyticsAdapter_getNetworkType": [
                        "    public static String getNetworkType(android.content.Context p3)",
                        "    {",
                        "        String v1;",
                        "        android.net.NetworkInfo v0 = com.ebay.nautilus.kernel.net.Connector.getConnectedNetworkInfo(p3);",
                        "        if (v0 != null) {",
                        "            switch (v0.getType()) {",
                        "                case 0:",
                        "                    v1 = \"cell\";",
                        "                    break;",
                        "                case 1:",
                        "                    v1 = \"wifi\";",
                        "                    break;",
                        "                case 9:",
                        "                    v1 = \"ethernet\";",
                        "                    break;",
                        "                default:",
                        "                    v1 = \"Unknown\";",
                        "            }",
                        "        } else {",
                        "            v1 = \"Unknown\";",
                        "        }",
                        "        return v1;",
                        "    }"
                    ]
                },
        ...
        }
    }


Manual
------

.. code-block:: sh

    worker@cf0c3ee3e7ca:/home/worker/androlyze$ ./androanalyze -h
    INFO: appending "androguard/" to sys.path
    usage: androanalyze [-h] [-idb IMPORT_DATABASE] [-rdb RESULT_DATABASE_NAME]
                        [-c CONFIG] [-q] [-v] [-vl VLOG] [-V] [--yes]
                        [--apks APKS [APKS ...] | --hashes HASHES [HASHES ...] |
                        --package-names PACKAGE_NAMES [PACKAGE_NAMES ...] | --tags
                        TAGS [TAGS ...]] [-pm {parallel,distributed,non-parallel}]
                        [--no-sort-code-size] [--concurrency CONCURRENCY] [-si]
                        [scripts [scripts ...]]

    positional arguments:
      scripts               The scripts to use for the security audit. If nothing
                            given, use defaults read from
                            conf/script_settings.json

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

    filter:
      --apks APKS [APKS ...]
                            The apk files or directories (with .apk files). Apk
                            files and directories can also be mixed. If non given,
                            use the imported apks. Will not import the apks into
                            the import database!
      --hashes HASHES [HASHES ...]
                            The hash of the apk from which you want to retrieve
                            information. If hash(es) are supplied, given package
                            names will be ignored !
      --package-names PACKAGE_NAMES [PACKAGE_NAMES ...]
                            The package names of the apks from which you want to
                            retrieve information.
      --tags TAGS [TAGS ...]
                            Only show infos for apks with specified tag(s)

    Parallelization parameters:
      -pm {parallel,distributed,non-parallel}, --parallelization-mode {parallel,distributed,non-parallel}
                            Choose the parallelization mode. If none supplied,
                            default value from config file will be used!
      --no-sort-code-size, -nscs
                            By default sort apks by code size (descending) ->
                            Analyze bigger code first. Use this switch to disable
                            this behavior
      --concurrency CONCURRENCY
                            Number of workers to spawn. Only for parallel mode
      -si, --send-id        Send id of apk file rather than actual file. Needs
                            import with -cdb first!
