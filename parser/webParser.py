"""
Controller to forward parsing calls to appropriate
web-site specific parser
"""
from leetcodeParser import LeetCodeParser


class WebParser(object):
    @staticmethod
    def parse_page(host, page_text):
        """
        Get the problem description from the supplied input page
        text
        :param host: web-site host name
        :param page_text: extracted source from the page.
        :return:
        """
        result_tag = None
        if 'leetcode' in host:
            result_tag = LeetCodeParser.parse_for_post(page_text)
        else:
            print "I can't find any appropriate parser for this host. Ping that damn developer to patch me up!!!"
        return result_tag

