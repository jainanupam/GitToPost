"""
Parse the code files (.java/.py etc) to get the link to
corresponding problem description page.
"""
import os


class CodeParser(object):
    def __init__(self):
        """
        initialize
        """
        self.pattern1 = r'/*'
        self.pattern2 = r'*/'

    def get_page_link(self, file_name):
        """
        Get the link to the problem description page from code file.
        :param file_name: code file to be parsed
        :return: link (if any) to the problem page
        """
        if '.java' in file_name:
            with open(file_name, 'r') as inf:
                line = inf.readline()
                # print line
                if self.pattern1 in line:
                    print file_name + " : " + line
                    link = line[line.index(self.pattern1) + 2: line.index(self.pattern2)]
                    # print link
                    return link


    def get_code(self, file_name):
        """
        Get the source code of the code file.
        :param file_name:
        :return: Source code from the file.
        """
        
        
# print os.getcwd()
'''
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
'''
