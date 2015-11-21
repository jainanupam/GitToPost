import os
import subprocess


def execGitCommand(repo_path, cmd='log'):
	pr = subprocess.Popen("git " + cmd, cwd = os.path.dirname(repo_path), shell = True, stdout = subprocess.PIPE,
						  stderr = subprocess.PIPE)
	(out, error) = pr.communicate()

	print "Error: " + error
	print "out: " + out 

# Sample call
execGitCommand(r"../Questions/Algo/java")