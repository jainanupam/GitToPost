"""
Controller to forward parsing calls to appropriate
web-site specific parser
"""
from leetcodeParser import LeetCodeParser
from geeksforgeeksParser import GeeksForGeeksParser


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
        try:
            if not post.host_name:
                print "No host name found in this post object"
                return result_tag
        except Exception:
            print "No host name found in this post object"
            return result_tag

        if 'leetcode' in post.host_name:
            result_tag = LeetCodeParser.parse(post)
        elif 'geeksforgeeks' in post.host_name:
            result_tag = GeeksForGeeksParser.parse(post)
        else:
            print "I can't find any appropriate parser for this host: " + post.host_name + \
                  ". Ping that damn developer to patch me up!!!"
        return result_tag

