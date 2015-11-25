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
        self.java_comment_start = r'/*'
        self.java_comment_end = r'*/'
        self.python_comment = r"'''"

    def get_page_link(self, file_name):
        """
        Get the link to the problem description page from code file.
        Returns None if no such link is found
        :param file_name: code file to be parsed
        :return: link (if any) to the problem page
        """
        if not os.path.isfile(file_name):
            return None
        with open(file_name, 'r') as inf:
            if '.java' in file_name:
                line = inf.readline()
                if self.java_comment_start in line:
                    # print file_name + " : " + line
                    link = line[line.index(self.java_comment_start) +
                                len(self.java_comment_start): line.index(self.java_comment_end)]
                    # print link
                    return link.strip()
            elif '.py' in file_name:
                # print "it's a py file"
                line = inf.readline()
                # print line
                if self.python_comment in line:
                    # print file_name + " : " + line
                    link = line[line.index(self.python_comment) +
                                len(self.python_comment): line.index(self.python_comment, len(self.python_comment))]
                    # print link
                    return link.strip()

            return None

    def get_code(self, file_name):
        """
        Get the source code of the code file.
        :param file_name:
        :return: Source code from the file.
        """
        file_text = ""
        with open(file_name, 'r') as inf:
            for line in inf:
            # line = inf.readline()
            # print line
                file_text += line

        return file_text

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
