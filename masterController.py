import logging
from makePost import make_post
from parser.codeParser import CodeParser
from parser.Fetcher import Fetcher
from parser.leetcodeParser import parse_for_post

file_name = r'/Users/anupamjain/code/gitRepo/Questions/Algo/Java/AddDigits.java'

code_parser = CodeParser()
link = code_parser.get_page_link(file_name)
print link

link = 'https://www.leetcode.com/problems/add-digits/ '
fetcher = Fetcher(logging.DEBUG)
response = fetcher.fetch(link)

# print response

result_tag = parse_for_post(response)

print result_tag

make_post(file_name, result_tag)

#print div_lst
