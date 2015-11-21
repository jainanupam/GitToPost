import logging
from makePost import make_post
from parser.codeParser import CodeParser
from parser.Fetcher import Fetcher
from parser.webParser import WebParser

file_name = r'/Users/anupamjain/code/gitRepo/Questions/Algo/Java/AddDigits.java'

code_parser = CodeParser()
link = code_parser.get_page_link(file_name)
print link

# link = 'https://www.leetcode.com/problems/add-digits/'
fetcher = Fetcher(logging.DEBUG)
host, response = fetcher.fetch(link.strip())

# print host
# print response

# Get the appropriate problem description
result_tag = WebParser.parse_page(host, response)

print result_tag
'''
make_post(file_name, result_tag)

#print div_lst
'''