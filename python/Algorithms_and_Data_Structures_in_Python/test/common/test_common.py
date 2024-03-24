import os
import sys
import glob
import subprocess


def spawn_python_script(script_path):
    params = [sys.executable, script_path]

    # Build the PYTHONPATH environment variable needed by the child process
    # in order to acquire the same sys.path values of the parent process.
    python_path = ":".join(sys.path)[1:] # strip leading colon
    return subprocess.run(params, env={'PYTHONPATH':python_path})

def find_test(path):
    path += "/unit-tests/*/*.py"
    return glob.iglob(path)

def append_src_paths():
    sys.path.append('./common')
    sys.path.append('../src/functions')
    sys.path.append('../src/structures')

def run_tests():
    test_script_paths = find_test(os.getcwd())

    for test_script_path in test_script_paths:
        # running other file using run()
        print(test_script_path)
        spawn_python_script(test_script_path)
        print ("----------")