Script Chaining
===============

Use the :py:class:`.ChainedScript` to chain multiple :py:class:`.AndroScript`

Either derive from it, or use the :py:func:`.chained_script` function to generate a :py:class:`.ChainedScript`

Have a  look at this example of a :py:class:`.ChainedScript` which chains scripts like :py:class:`.Activities`, :py:class:`.Services`, :py:class:`.Permissions` etc:

.. literalinclude:: androlyze/androlyze/model/script/impl/ChainedApkInfos.py


There are 5 interesting methods you should see:

* :py:meth:`.ChainedScript.root_categories`

* :py:meth:`.ChainedScript.chain_scripts`

* :py:meth:`.ChainedScript.log_chained_script_meta_infos`.

	.. code-block:: sh

	    "ChainedScript": {
	        "scripts": [
	            "ChainedApkInfos",
	            "dvm"
	        ],
	        "successful": [
	            "ChainedApkInfos"
	        ],
	        "failures": [
	        	"dvm"
	                ]
	            }
	        ]
	    }

* :py:meth:`.ChainedScript.continue_on_script_failure`

* :py:meth:`.ChainedScript.log_script_failure_exception`. Example:

	.. code-block:: sh

	    "ChainedScript": {
	        "scripts": [
	            "ChainedApkInfos",
	            "dvm"
	        ],
	        "successful": [
	            "ChainedApkInfos"
	        ],
	        "failures": [
	            {
	                "dvm": [
	                    "Traceback (most recent call last):\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/model/script/ChainedScript.py\", line 71, in _analyze\n    script_result = ascript.analyze(apk, dalvik_vm_format, vm_analysis, gvm_analysis, *args, **kwargs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/model/script/AndroScript.py\", line 120, in analyze\n    time_s = timeit(self._analyze, *((apk, dalvik_vm_format, vm_analysis, gvm_analysis) +  args), **kwargs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/util/Util.py\", line 165, in timeit\n    res = func(*args, **kwargs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/model/script/ChainedScript.py\", line 71, in _analyze\n    script_result = ascript.analyze(apk, dalvik_vm_format, vm_analysis, gvm_analysis, *args, **kwargs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/model/script/AndroScript.py\", line 120, in analyze\n    time_s = timeit(self._analyze, *((apk, dalvik_vm_format, vm_analysis, gvm_analysis) +  args), **kwargs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/util/Util.py\", line 165, in timeit\n    res = func(*args, **kwargs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androlyze/model/script/impl/Disassembly.py\", line 42, in _analyze\n    ms.process()\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androguard/androguard/decompiler/dad/decompile.py\", line 105, in process\n    register_propagation(graph, uses, defs)\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androguard/androguard/decompiler/dad/dataflow.py\", line 241, in register_propagation\n    logger.debug('  Used vars: %s', ins.get_used_vars())\n",
	                    "  File \"/home/nils/Dropbox/androlyze/androguard/androguard/decompiler/dad/instruction.py\", line 392, in get_used_vars\n    lused_vars.extend(v_m[self.rhs].get_used_vars())\n",
	                    "KeyError: 0\n"
	                ]
	            }
	        ]
	    }


.. literalinclude:: androlyze/androlyze/model/script/ChainedScript.py	    
