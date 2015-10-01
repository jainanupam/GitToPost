import os
import subprocess
#import sys
#import commands

pr = subprocess.Popen("/usr/bin/git log", cwd = os.path.dirname('/Users/anupam336971/code/gitRepo/Questions/'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
(out, error) = pr.communicate()

print "Error: " + error
print "out: " + out 
