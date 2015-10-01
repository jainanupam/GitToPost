import os

#print os.getcwd()
dir_path = '/Questions/Algo'
os.chdir('../..' + dir_path)

file_name = 'BinaryTreePaths.java'
pattern1 = r'/*'
pattern2 = r'*/'
file_list = os.listdir('.')
for file_name in file_list:
    if '.java' in file_name:
        with open(file_name, 'r') as inf:
            line = inf.readline()
            #print line
            if pattern1 in line:
                print file_name + " : " + line
                print line[line.index(pattern1) + 2: line.index(pattern2)]
