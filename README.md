# GitToPost
Project to parse git repo and prepare posts for website

### Main file
masterController.py

### Executing gitCaller.py
python -c 'import gitCaller; gitCaller.execGitCommand("Your repo path goes here/")'

### TODO
- [x] Parse the code files to get the links(if any) from the files for problem source.  
 - [ ] Store the file and corresponding link.  
- [x] Fetch and parse the page from the above URL to get the problem description.  
- [x] Prepare the post file.  
