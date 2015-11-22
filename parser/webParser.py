"""
Controller to forward parsing calls to appropriate
web-site specific parser
"""
from leetcodeParser import LeetCodeParser


class WebParser(object):
    @staticmethod
    def parse_page(post):
        """
        Get the problem description from the supplied input page
        text
        :param post: the post object
        :return:
        """
        result_tag = None
        if 'leetcode' in post.host_name:
            result_tag = LeetCodeParser.parse(post)
        else:
            print "I can't find any appropriate parser for this host. Ping that damn developer to patch me up!!!"
        return result_tag

