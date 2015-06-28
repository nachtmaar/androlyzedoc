
******
Docker
******

For ease of use, we enable the deployment with Docker. 

`AndroLyze` comes with a few docker images which ship the distributed system, consisting of a message queue ( `RabbitMQ <https://www.rabbitmq.com>`_ ), a NoSQL database ( `mongoDB <https://www.mongodb.com>`_ ) and the actual worker node.


Before you can start playing with Docker you need to clone the repository:

.. code-block:: sh

	$ git clone --recursive https://github.com/nachtmaar/androlyze.git
	$ cd androlyze

Config
======

`AndroLyze` has one important config file which lets you customize the distributed system. The credentials defined there are used by the rabbitmq and mongodb container. At startup, they grab the relevant information from the config file and set up the appropriate user/access.

The IPs and Ports specified in the config don't have to be set when using Docker due to the Docker linking system.

If you plan to use `AndroLyze` on Amazon EC2, you should consider using S3 for APK storage. For this purpose you have to set the Amazon access id and key!


Docker installation
===================

The installation with Docker requires Linux. On Mac have a look at `boot2docker <http://boot2docker.io>`_ which uses a linux virtual machine to enable the usage of Docker.

Linux:

.. code-block:: sh

	
	$ sudo apt-get install docker.io
	
Mac:

.. code-block:: sh

	$ brew install boot2docker
	$ boot2docker init
	$ boot2docker up
	
Now set the environment variables as instructed by the output of the up command.

.. note::

	The following docker commands require sudo on Linux but not OS X!

Data container
==============

The config file, APKs and import databases are shared with all containers through a `data container <https://docs.docker.com/userguide/dockervolumes/>`_. 

.. note::

	For OS X be aware that folders mounted with the "-v" switch have to live in your home folder as a restriction of boot2docker!

Create and adopt your `AndroLyze` config file to your needs:

.. code-block:: sh

	$ cp androlyze/settings/defaults/config.conf data_container/
	$ vim data_container/config.conf

The default config is suitable for a local run using Docker. Nothing has to be changed, but can of course.

Start the data container (and supply a custom directory for the APKs and import databases which shall be mounted into the container and lives inside the host os):

.. code-block:: sh

	$ docker create -v $PWD/data_container:/etc/androlyze  -v <Full Path to APK Directory>:/home/worker/androlyze/apks -v <Full Path to Import Databases>:/home/worker/androlyze/dbs --name data nachtmaar/androlyze_worker:latest /bin/true
	fc0abfe19883fd48657275a16c988195a49a94fac8aaf52e1d07a8b67a371507

Create X.509 certificates
=========================

`AndroLyze` can be secured with X.509 certificates. The following container creates the necessary CA, server and client certificates and stores them in `conf/distributed/ssl` of the `AndroLyze` source folder.

.. note::
	
	By default `AndroLyze` is setup with randomly created self-signed certificates!

	If you want to use your own PKI, just place `androlyze_ca.pem`, `androlyze_server.crt`, `androlyze_server.key`, `androlyze_client.key` and `androlyze_client.crt` into the data_container folder.

	Moreover you should pin the `AndroLyze` Certificate Authority! On Mac OS just double click the `androlyze_ca.pem` file.
	
Start a container which sets up the whole Public Key Infrastructure:

.. code-block:: sh

	$ docker run --rm -it -v $PWD/data_container:/usr/share/easy-rsa/keys_androlyze nachtmaar/androlyze_x_509:latest

.. code-block:: sh

	$ ls data_container
	01.pem			androlyze_client.key	ca.crt			index.txt		serial
	02.pem			androlyze_server.crt	ca.key			index.txt.attr		serial.old
	androlyze_client.crt	androlyze_server.csr	config.conf		index.txt.attr.old
	androlyze_client.csr	androlyze_server.key	dh2048.pem		index.txt.old


Other containers
================

For the first try, we run the containers interactively so that we can follow the stdout/stderr of each container.
For each of the 4 shell commands spawn a new shell and execute the command.
If you stop a container with CTLR-C the image of the container gets deleted (removing the "--rm" switch keeps the images)

Run the NoSQL database (mongoDB):

.. code-block:: sh
	
	# The command exposes port 27017 so that mongoDB can be accessed from the containers host system
	$ docker run -it --rm --name mongodb -p 27017:27017 --volumes-from data nachtmaar/androlyze_mongodb:latest

Run the message queue (RabbitMQ):

.. code-block:: sh

	# The command exposes port 15672 so that the rabbitmq management webui can be accessed from the containers host system
	$ docker run -it --rm --name rabbitmq -p 15672:15672 --volumes-from data nachtmaar/androlyze_rabbitmq:latest

Run celery flower, a monitoring tool for the distributed system.

.. code-block:: sh

	# The command exposes port 5555 so the webui of celery flower can be accessed from the containers host system
	$ docker run -it --rm --name flower -p 5555:5555 --volumes-from data --link rabbitmq:rabbitmq --link mongodb:mongodb nachtmaar/androlyze_flower:latest

.. warn::

	 Be aware that the web service of celery flower is not secured with https!
	 The container is not an essential part of `AndroLyze` and can be left out in production!

Run the worker and link the database as well as the message queue so that they know from each other

.. code-block:: sh

	$ docker run -it --rm --name worker --volumes-from data --link rabbitmq:rabbitmq --link mongodb:mongodb nachtmaar/androlyze_worker:latest

That's it
=========

All containers need some time to initialize themselves. Especially the worker and flower container need to pull code from git (secured with https or ssh key verification for private repos).

In the status_ section you can check how the logs of the containers should look like if you encounter any error.

If everything went right, you can connect to the frontend container:

.. code-block:: sh

	$ docker exec -it worker bash
	export TERM=xterm

Moreover, you should be able to visit the RabbitMQ management service on port 15672 and the flower monitoring service on port 5555 (see the Monitoring / Management section)

Status
======

.. _status:

Afterwards the following containers should run:

.. code-block:: sh

	$ docker ps
	CONTAINER ID        IMAGE                                  COMMAND                CREATED             STATUS              PORTS                                NAMES
	e3f1673b2c9d        nachtmaar/androlyze_worker:latest     "/bin/sh -c ./start.   5 seconds ago       Up 3 seconds                                             worker
	31ac00f6fc35        nachtmaar/androlyze_flower:latest     "/bin/sh -c ./start.   9 seconds ago       Up 7 seconds        0.0.0.0:5555->5555/tcp               flower
	3ec8edb7ce56        nachtmaar/androlyze_rabbitmq:latest   "/sbin/my_init"        13 seconds ago      Up 11 seconds       5672/tcp, 0.0.0.0:15672->15672/tcp   rabbitmq
	e91abaa7d1da        nachtmaar/androlyze_mongodb:latest    "/sbin/my_init"        18 seconds ago      Up 16 seconds       0.0.0.0:27017->27017/tcp             mongodb

The output of the containers look like this:

MongoDB
-------

.. code-block:: sh

	configuring mongodb [done]

	configuring ssl ...
	configuring ssl [done]
	starting mongodb ...
	Sat Jun 20 11:38:35.385 [initandlisten] MongoDB starting : pid=14 port=27017 dbpath=/data/db/ 64-bit host=55d3e0780db4
	Sat Jun 20 11:38:35.385 [initandlisten] db version v2.4.9
	Sat Jun 20 11:38:35.386 [initandlisten] git version: nogitversion
	Sat Jun 20 11:38:35.386 [initandlisten] build info: Linux orlo 3.2.0-58-generic #88-Ubuntu SMP Tue Dec 3 17:37:58 UTC 2013 x86_64 BOOST_LIB_VERSION=1_54
	Sat Jun 20 11:38:35.386 [initandlisten] allocator: tcmalloc
	Sat Jun 20 11:38:35.386 [initandlisten] options: { dbpath: "/data/db/", smallfiles: true, sslCAFile: "/etc/androlyze/androlyze_ca.pem", sslOnNormalPorts: true, sslPEMKeyFile: "/etc/ssl/private/mongodb.pem", sslWeakCertificateValidation: true }
	Sat Jun 20 11:38:35.388 [initandlisten] journal dir=/data/db/journal
	Sat Jun 20 11:38:35.388 [initandlisten] recover : no journal files present, no recovery needed
	Sat Jun 20 11:38:35.457 [initandlisten] waiting for connections on port 27017 ssl
	Sat Jun 20 11:38:35.459 [websvr] admin web console waiting for connections on port 28017 ssl

RabbitMQ
--------

.. code-block:: sh

	Server startup complete; 6 plugins started.
	 * amqp_client
	 * mochiweb
	 * rabbitmq_management
	 * rabbitmq_management_agent
	 * rabbitmq_web_dispatch
	 * webmachine
	 completed with 6 plugins.

	=INFO REPORT==== 20-Jun-2015::14:25:31 ===
	accepting AMQP connection <0.331.0> (172.17.0.229:59456 -> 172.17.0.228:5671)

	=INFO REPORT==== 20-Jun-2015::14:25:31 ===
	accepting AMQP connection <0.337.0> (172.17.0.229:59457 -> 172.17.0.228:5671)

Flower 
------

.. code-block:: sh

	[I 150617 17:29:49 command:114] Visit me at http://0.0.0.0:5555
	[I 150617 17:29:49 command:116] Broker: amqp://androlyze:**@172.17.0.177:5672/androlyze_vhost
	[I 150617 17:29:49 command:119] Registered tasks:
	    ['androlyze.analyze.distributed.tasks.AnalyzeTask.AnalyzeTask',
	     'celery.backend_cleanup',
	     'celery.chain',
	     'celery.chord',
	     'celery.chord_unlock',
	     'celery.chunks',
	     'celery.group',
	     'celery.map',
	     'celery.starmap']
	[I 150617 17:29:49 mixins:225] Connected to amqp://androlyze:**@172.17.0.177:5672/androlyze_vhost

Worker
------

.. code-block:: sh

	 -------------- celery@31fb65be6c49 v3.1.18 (Cipater)
	---- **** -----
	--- * ***  * -- Linux-3.18.11-tinycore64-x86_64-with-Ubuntu-14.04-trusty
	-- * - **** ---
	- ** ---------- [config]
	- ** ---------- .> app:         AndroLyze:0x7f57d457b3d0
	- ** ---------- .> transport:   amqp://androlyze:**@172.17.1.111:5671/androlyze_vhost
	- ** ---------- .> results:     rpc
	- *** --- * --- .> concurrency: 4 (prefork)
	-- ******* ----
	--- ***** ----- [queues]
	 -------------- .> analyze_apk      exchange=celery(direct) key=analyze_apk
	                .> celery           exchange=celery(direct) key=celery

	[2015-06-18 21:20:54,523: WARNING/MainProcess] celery@31fb65be6c49 ready.

Starting/stopping
=================

All containers can be simply stopped and start after they have been created the first time. But for this you need to create all the containers without the "--rm" switch!


Stop them:

.. code-block:: sh

	docker stop flower worker rabbitmq mongodb data

Start them:

.. code-block:: sh

	# be sure to start the services before flower and the worker (they need the correct ip and port of the services)
	docker start data mongodb rabbitmq flower worker


Development
===========

Docker can also be used to ease development. For this purpose, it is necessary to have a local clone of `AndroLyze` so that the development code can be mounted into `/home/worker/anrolyze` of the container.
If a repository is already existing in the container, it won't clone the code from git again as it normally does if no source code is mounted into the container.

Changes in the source code (done outside the container) affect the source in the container. Otherwise one would need to push changes to git and check it out then. Or develop in the container itself.

.. code-block:: sh

	docker run -it --rm --name worker -v /Users/nils/Desktop/androlyze/:/home/worker/androlyze --volumes-from data --link rabbitmq:rabbitmq --link mongodb:mongodb nachtmaar/androlyze_worker:latest
