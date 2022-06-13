import subprocess

#subprocess.call(["calc"], shell=True)
#out = subprocess.check_call(["cmd", "/c", "ssd"])
#don't enable code execution by passingput to a dangerous function

out = subprocess.check_output(["cmd", "/c", "whoami"])
print(out.decode())