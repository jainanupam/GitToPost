import os
import logging
import ConfigParser
from makePost import make_post, append_to_post
from post import Post
from verifyUnique import VerifyUnique
from parser.codeParser import CodeParser
from parser.Fetcher import Fetcher
from parser.webParser import WebParser


def process_file(file_name, out_dir):
    code_parser = CodeParser()
    link = code_parser.get_page_link(file_name)
    if not link:
        print "I can't find any link in the given file"
        return
    # link = 'https://www.leetcode.com/problems/add-digits/'

    # initialize the post
    post = Post(link=link, file_name=file_name)

    # Check for post uniqueness for current file
    verify_unique = VerifyUnique(config)
    status = verify_unique.check_post_exists(post)
    if status is verify_unique.NON_UNIQUE:
        print 'post file already exists'
    elif status is verify_unique.NEW_CODE:
        # Append the current code existing post file.
        append_to_post(post.post_file, file_name)
        print "updated already existing post file for: " + file_name
    else:
        fetcher = Fetcher(logging.DEBUG)
        host, response = fetcher.fetch(link.strip())

        # print host
        # print response

        post.host_name = host
        post.raw_page = response

        # Get the appropriate problem description
        problem_desc_tag = WebParser.parse_page(post)
        # update the post object
        post.problem_text = problem_desc_tag
        # print 'title: ' + post.title
        # print problem_desc_tag
        if not problem_desc_tag:
            # print "could not parse the file "
            return
        make_post(file_name, post, out_dir)
        verify_unique.serialize_post(post)

        print "Created new post file"

    # print div_lst


# file_name = r'/Users/anupamjain/code/gitRepo/Questions/Algo/Java/AddDigits.java'
# file_name = r'/Users/anupamjain/code/gitRepo/Questions/Algo/python/BullsAndCows.py'

config = ConfigParser.ConfigParser()
config.read('config.cfg')
parent_dir = config.get('Paths', 'input_dir')
parent_out_dir = config.get('Paths', 'output_dir')

'''
process_file(file_name, parent_out_dir)
'''
# print config.items('Sub-dir')
# Loop over each sub-dir to reach to all input files in each dir

for sub_dir in config.items('Sub-dir'):
    print "\nGoing through: " + sub_dir[1] + " folder..."
    input_dir = parent_dir + sub_dir[1]
    # print os.listdir(input_dir)
    file_list = os.listdir(input_dir)
    i = 0
    for f in file_list:
        i += 1
        file_name = input_dir + f
        print '\n' + file_name
        process_file(file_name, parent_out_dir + sub_dir[1])
        # if i > 20:
        #     break
    print "========================================"
    print "Total files checked : " + str(i)

'''
# '''
