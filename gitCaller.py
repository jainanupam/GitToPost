import os
import subprocess

def execGitCommand(repoPath, cmd='log'):
	pr = subprocess.Popen("git " + cmd, cwd = os.path.dirname(repoPath), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	(out, error) = pr.communicate()

	print "Error: " + error
	print "out: " + out 
