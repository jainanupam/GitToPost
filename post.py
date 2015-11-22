"""
Plain object to hold and transfer post related data.
"""


class Post(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
