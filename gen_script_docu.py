#!/usr/bin/env python

import glob, os
import subprocess
import fnmatch

os.chdir("..")
print os.getcwd()

DOCU_DIR="androlyzelabdoc/script_docu"
SCRIPTS_DIR="scripts_builtin"
APK="com.spotify.music"

template = """
%s
%s
%s
          
This is an autogenerated documentation file for the script: %s

Run it
------

.. code-block:: sh

\t$ %s

%s

View the results
----------------

Non-Binary
``````````

.. code-block:: python

\t$ %s

    %s

Binary
``````

For the case that the result may exceed 16MB, it is stored in MongoDB's gridFS. Therefore we need to use a different query syntax:

View the meta data:

.. code-block:: python

\t$ %s

    %s

View the raw data:

.. code-block:: python

\t$ %s

    %s

Source
------

.. literalinclude:: ../androlyze/%s


"""

def indent(what, width=4):
    return "".join(["\t %s\n" %x for x in what.split("\n")])

def run(command):
    print(">>> %s" % command)
    #os.system(command)
    res = subprocess.check_output(command.split(" "))
    return res[:100000]
 
script_names = [] 
for root, dirnames, filenames in os.walk(SCRIPTS_DIR):
    for file in fnmatch.filter(filenames, '*.py'):
        if "__init__" not in file:# and "ASTifyMethodsText" not in file:
            print(file)
	    script_names.append(os.path.join(root, file))
            #matches.append(os.path.join(root, filename))


#run("./androanalyze %s --package-names %s -pm parallel" % (' '.join(script_names), APK))


for file in script_names:

        sname = file.split("/")[-1].split(".py")[0]
        with open("%s/%s.rst" % (DOCU_DIR, sname), "w") as f:
            
            cmd_ana = "./androanalyze %s/%s.py --package-names %s" % (SCRIPTS_DIR, sname, APK)
            #res_ana = run(cmd_ana)
            cmd_query = "./androquery result -sn %s -pn %s" % (sname, APK)
            res_query = run(cmd_query + " -l")

            cmd_query_nd = "./androquery result -sn %s -pn %s -nd" % (sname, APK)
            res_query_nd = run(cmd_query_nd + " -l")      

            cmd_query_ndr = "./androquery result -sn %s -pn %s -nd -r" % (sname, APK)
            res_query_ndr = run(cmd_query_ndr + " -l")      
	    if not res_query: res_query = "Empty"
	    if not res_query_nd: res_query_nd = "Empty"
	    if not res_query_ndr: res_query_ndr = "Empty"

            f.write(template % ("*" * len(sname), sname, "*" * len(sname),
                                sname,
                                cmd_ana, "",
                                cmd_query, indent(res_query),
                                cmd_query_nd, indent(res_query_nd),
                                cmd_query_ndr, indent(res_query_ndr),
                                file))

    
