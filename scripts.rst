Writing A Script
================

.. toctree::
	:maxdepth: 2

	script_requirements
	script_logging
	script_template
	script_chaining

The heart of `AndroLyze` are the scripts which provide the analysis functionality based on androguard.
Analysis results can be stored easily with the logging framework which is directly connected to the result database.

Scripts can be written in a very modular way and chained together to provide the final result. We call this `Script Chaining`.

During the script development one can test it locally to ensure it is correct before running it the first time on a cluster or in the cloud.

The following sites provide a more depth understanding how scripts work and how a new script can be written.



