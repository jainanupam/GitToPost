"""
Plain object to hold and transfer post related data.
"""


class Post(object):
    def __init__(self, **kwargs):
        """
        :param kwargs: host_name, link, raw_page, file_name, title,
        problem_text, files_covered, post_file
        :return:
        """
        self.__dict__ = kwargs
