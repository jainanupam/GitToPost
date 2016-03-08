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
    """

    :param file_name: fully qualified name of the file to be processed
    :param out_dir: Output directory to put the post in.
    :return: None
    """
    code_parser = CodeParser()
    link = code_parser.get_page_link(file_name)
    if not link:
        print "I can't find any link in the given file"
        return
    # link = 'https://www.leetcode.com/problems/add-digits/'

    # initialize the post
    post = Post(link=link, file_name=file_name)

    # Object of Uniqueness checker
    verify_unique = VerifyUnique(config)
    # Check for post uniqueness for current file
    status = verify_unique.check_post_exists(post)
    if status is verify_unique.NON_UNIQUE:
        print 'post file already exists'
    elif status is verify_unique.NEW_CODE:
        # Old post file already exists.
        # Append the current code to existing post file.
        append_to_post(post.post_file, file_name)
        print "updated already existing post file for: " + file_name
    else:
        # Object to fetch the web page
        fetcher = Fetcher(logging.DEBUG)
        # Get the host and web page from the link
        try:
            host, response = fetcher.fetch(link.strip())
        except Exception as e:
            print "Exception while fetching for link: ", link
            print "Exception: ", e
            return

        # print host
        # print response

        # update the post with host_name and
        # raw_page response values
        post.host_name = host
        post.raw_page = response

        # Get the appropriate problem description
        try:
            problem_desc_tag = WebParser.parse_page(post)
        except Exception, e:
            print "Exception in parsing page: ", e
            problem_desc_tag = None

        # print 'title: ' + post.title
        # print problem_desc_tag
        if not problem_desc_tag:
            print "could not parse the file "
            return
        # update the post object with problem description
        post.problem_text = problem_desc_tag
        # Save the post file
        print "making the post"
        try:
            make_post(file_name, post, out_dir)
            verify_unique.serialize_post(post)
        except Exception, e:
            print "could not make the post file", e
            return

        print "Created new post file"

    # print div_lst


# test file names
# file_name = r'/Users/anupamjain/code/gitRepo/Questions/Algo/Java/AStarSearchSquareGridWithWeight.java'
# file_name = r'/Users/anupamjain/code/gitRepo/Questions/Algo/python/BullsAndCows.py'

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.cfg')

# Get the input and output directories from config file
parent_dir = config.get('Paths', 'input_dir')
parent_out_dir = config.get('Paths', 'output_dir')

# move the posted files
verifyUnique = VerifyUnique(config)
verifyUnique.move_posted_files()

'''
# test for single file
process_file(file_name, parent_out_dir)
'''
# print config.items('Sub-dir')

# Loop over each sub-dir to reach to all input files in each dir

for sub_dir in config.items('Sub-dir'):
    print "\nGoing through: " + sub_dir[1] + " folder..."
    input_dir = parent_dir + sub_dir[1]
    # print os.listdir(input_dir)
    # Get list of all (code) files in current input directory
    file_list = os.listdir(input_dir)
    i = 0
    # Loop through all the code files
    for f in file_list:
        i += 1
        file_name = input_dir + f
        print '\n' + file_name
        # process the current file for making/ modifying the post
        process_file(file_name, parent_out_dir + sub_dir[1])
        # if i > 20:
        #     break
    print "========================================"
    print "Total files checked : " + str(i)

'''
# '''
