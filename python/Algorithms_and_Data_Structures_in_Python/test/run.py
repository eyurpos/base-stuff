import sys
import glob
import subprocess

sys.path.append('.')
sys.path.append('../src/functions')

def __spawn_python_script(script_path):
    params = [sys.executable, script_path]

    # Build the PYTHONPATH environment variable needed by the child process
    # in order to acquire the same sys.path values of the parent process.
    python_path = ":".join(sys.path) # strip leading colon
    return subprocess.run(params, env={'PYTHONPATH':python_path})


for test_script_path in glob.iglob("./*/*.py"):
    # running other file using run()
    print(test_script_path)
    __spawn_python_script(test_script_path)
    print ("----------")
