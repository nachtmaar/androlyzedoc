********
Manually
********

Install AndroLyze
-----------------

.. code-block:: sh
	
	# clone recursive to fetch submodules
	git clone --recursive https://ds.mathematik.uni-marburg.de/gitlab/android/androlyze.git
	
	cd androlyze

	# copy the sample config file
	cp androlyze/settings/defaults/config.conf conf/
	cp androlyze/settings/defaults/script_settings.json conf/
	
	# copy config for google-play-crawler (needed for playstore.py)
	cp google-play-crawler/googleplay/crawler.conf conf/

	# revoke not needed permissions for config files (contains credentials)
	chmod 600 -R conf/

Install other requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

	# install pip
	sudo apt-get install python-pip

	# install mongodb python driver
	pip install --user -r docker/worker/requirements.txt

Distributed Environment
-----------------------

.. code-block:: sh

	# install celery
	sudo pip install celery

	# only for task server
	sudo apt-get install rabbitmq-server

	sudo apt-get install mongodb

	# needed for worker clients (dependency of androguard)
	sudo pip install ipython

MongoDB
```````

Also see `MongoDB installation <http://docs.mongodb.org/manual/installation/>`_


Authentication and SSL
``````````````````````

.. note::

	The user creation shown below is for MongoDB version 2.4, 2.2 is a different API !
	For version 3 one has to use `db.createUser` instead of `db.addUser` but with the same arguments!

First we need to add an account. One for user administration, second for database r/w access.

.. code-block:: sh
	
	# start the mongo shell
	mongo <host>

.. code-block:: sh

	use admin
	# add useradmin
	db.addUser( { user: "useradmin",
	              pwd: "pwd",
	              roles: [ "userAdminAnyDatabase"] } )

	# add androlyze user (needs full access to create user supplied databases via config file)
	db.addUser( { user: "androlyze",
	              pwd: "pwd",
	              roles: [ "readWriteAnyDatabase"] } )

Enable authentication in config file (/etc/mongodb.conf)

.. code-block:: sh

	# mongodb.conf

	# Where to store the data.
	dbpath=/var/lib/mongodb

	#where to log
	logpath=/var/log/mongodb/mongodb.log

	logappend=true

	bind_ip = 127.0.0.1
	port = 27017

	# Enable journaling, http://www.mongodb.org/display/DOCS/Journaling
	journal=true

	auth = true

For X509 certificate creation have a look at `RabbitMQ website <https://www.rabbitmq.com/ssl.html>`_.
For SSL add these values too:

.. code-block:: sh

	# SSL options
	sslMode = requireSSL

	# SSL Key file and certificate
	sslPEMKeyFile = /etc/ssl/private/mongodb/mongodb.pem

	sslOnNormalPorts = true

	# ca certificate
	sslCAFile = /etc/ssl/certs/androlyze_ca.pem

	# client don't need a certificate
	sslWeakCertificateValidation = true

Restart server

.. code-block:: sh

	sudo /etc/init.d/mongodb restart

.. warning::
		
	If you are encountering any troubles with starting the mongodb server,
	try to start it manually with mongod --config /etc/mongodb.conf
	and have a look at the log file.

	or test with
	sudo -u mongodb mongod --config /etc/mongodb.conf


RabbitMQ
^^^^^^^^

RabbitMQ configuration (see `this <http://celery.readthedocs.org/en/latest/getting-started/brokers/rabbitmq.html>`_ for more details):

.. code-block:: sh

 	sudo rabbitmqctl add_user androlyze <pw>
	sudo rabbitmqctl add_vhost androlyze
	sudo rabbitmqctl set_permissions -p androlyze_vhost androlyze  ".*" ".*" ".*"
	

Extra space
```````````
We need a big task storage, so if your root disk is not big enough use some different path.
Default is /var/lib/rabbitmq.

Set in file "/etc/rabbitmq/rabbitmq-env.conf"

.. code-block:: sh

	RABBITMQ_MNESIA_BASE=/custompath/lib/rabbitmq/


SSL
```

For X509 certificate creation have a look at `RabbitMQ website <https://www.rabbitmq.com/ssl.html>`_.

File: /etc/rabbitmq/rabbitmq.config

.. code-block:: sh

	[
	  {rabbit, [
	     {tcp_listeners, []},
	     {ssl_listeners, [5671]},
	     {ssl_options, [{cacertfile,"/etc/ssl/certs/androlyze_ca.pem"},
	                    {certfile,"/etc/ssl/certs/androlyze_server.pem"},
	                    {keyfile,"/etc/ssl/private/rabbitmq/androlyze_server.key"},
	                    {verify,verify_peer},
	                    {fail_if_no_peer_cert,true}]}
	   ]}
	].


.. warning::

	For errors have a look at the log file:

	tail -n 50 /var/log/rabbitmq/rabbit....log


Distributed config
``````````````````
There is an extra config file for the distributed environment.
Its located at androlyze/settings/defaults/distributed.conf

.. literalinclude:: ../androlyze/settings/defaults/distributed.conf


Deployment and Management
-------------------------
Fabric uses ssh to connect to the workers and executes the tasks locally on them.
Therefore you need to do set a few values in the Deployment section of the distributed config file.

.. code-block:: sh

	Available fabric commands:

	    cnt_processes         Cnt "celery worker" processes
	    deploy_project        If `user` and/or `passwd` given, use them to authenticate when cloning via http.
	    deploy_scripts        Deploy the scripts on the workers. `scripts_src` is the script folder what shall be synced
	    deploy_testing        Deploy the testing code on the workers. Intended for usage where changes have not been comitted (or not to master)
	    initial_worker_setup  Initial worker setup. Needs root access.
	    install_dependencies  Set up the workers
	    kill_processes        Kill the workers by sending the kill signal.
	    list_processes        List "celery worker" processes
	    restart_workers       Restart workers on registered hosts with specified concurrency.
	    start_workers         Start workers on registered hosts with specified concurrency.
	    stop_workers          Stop all workers.


Examples
````````

.. code-block:: sh

	# uses the username specified in config file or your username
	fab start_workers

	# don't try public-key auth
	fab start_workers -k 

	# use worker as username
	# otherwise
	fab start_workers -u worker

	# you can also use hosts other than in the config file
	fab start_workers -H user@worker

	# restart workers with default concurrency=#number of cores
	fab restart_workers

	# custom conurrency
	fab restart_workers:concurrency=16

	# use autoscaling, min: #number of cores, max: min * multiplicator
	fab restart_workers:autoscale=True,autoscale_mult=2

	# kill workers
	fab kill_processes

	# deploy scripts on workers
	fab deploy_scripts:userscripts/nils/

.. warning::

	.. code-block:: sh

		# don't use! it will wipe the scripts from other users!
		fab deploy_scripts:userscripts
