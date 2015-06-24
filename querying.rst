Querying
========

Now that we imported the APKs we can query the import database:

.. code-block:: sh

    worker@cf0c3ee3e7ca:/home/worker/androlyze$ ./androquery import infos-all
    INFO: appending "androguard/" to sys.path
    air.de.fahren_lernen.app 3.2.19
        sha256: 913d779289eae02c6712515ce42f89b353f4f2faf645d398ccbe484f662439da
        import date: 2015-06-20 20:07:33
        path: /home/worker/androlyze/apks/02.03.2015_top_free_4/apps_topselling_free/EDUCATION/air.de.fahren_lernen.app.apk
        code size: 435352
        build date: 2015-01-19 12:19:18
    air.nn.mobile.app.main 1.4.20
        sha256: 52c7c1974fc4d87821e88a28a36a66f4e78aa23ca0693d88a7bb00ffa1869fb7
        import date: 2015-06-20 20:07:35
        path: /home/worker/androlyze/apks/02.03.2015_top_free_4/apps_topselling_free/EDUCATION/air.nn.mobile.app.main.apk
        code size: 2852236
        build date: 2014-12-05 17:50:42

    ...

Manual
------

.. code-block:: sh

    worker@cf0c3ee3e7ca:/home/worker/androlyze$ ./androquery import --help
    INFO: appending "androguard/" to sys.path
    usage: androquery import [-h] [--all]
                             {infos,infos-all,versions,paths,package-names,hashes}
                             ...

    positional arguments:
      {infos,infos-all,versions,paths,package-names,hashes}
                            Available query commands for import db
        infos               List apks (short description)
        infos-all           List apks (detailed description)
        versions            List versions
        paths               List paths
        package-names       List package names
        hashes              List hashes of apks

    optional arguments:
      -h, --help            show this help message and exit
      --all                 Select whole database.



