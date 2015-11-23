"""
Check whether the current file/link being
checked is unique or if there already is
a file related to this post.
"""
import os
# imports for testing purpose
import ConfigParser
from post import Post


class VerifyUnique(object):
    def __init__(self, config):
        self.__dict__ = {'IS_UNIQUE': 0, 'NEW_CODE': 1, 'NON_UNIQUE': 2}
        parent_out_dir = config.get('Paths', 'output_dir')
        self.serialized_objects_path = parent_out_dir + 'posts-serial/'
        self.files = set(os.listdir(self.serialized_objects_path))

    def check_post_exists(self, post):
        """
        Check whether the given post already exists or not.
        :param post:
        :return:
        """
        # Get the link's hash (for that is the unique key)
        link_code = VerifyUnique.__get_hash(post.link)
        # print 'link hash: ' + link_code

        file_name = self.serialized_objects_path + link_code

        # Check if the hash exists in the self.files
        # print self.files
        if link_code not in self.files:
            # If not exists, serialize this post and return True1
            post.files_covered = set()
            post.files_covered.add(post.file_name)
            VerifyUnique.__serialize_post(file_name, post)
            return self.IS_UNIQUE

        # If it does, need to unpickle the existing object
        deserialized_post = VerifyUnique.__deserialize_post(file_name)

        # print deserialized_post.host_name, deserialized_post.link, \
        #    deserialized_post.file_name, deserialized_post.files_covered

        # Check if the unpickle object has the current code
        # file in it's list. if yes, return False
        if post.file_name in deserialized_post.files_covered:
            return self.NON_UNIQUE

        # print post.file_name
        # If not, update the old object with current file.
        deserialized_post.files_covered.add(post.file_name)

        VerifyUnique.__serialize_post(file_name, deserialized_post)

        post.post_file = deserialized_post.post_file

        return self.NEW_CODE
        # Should pickle/ unpickle be included as part of this?
        # (YES)

    def serialize_post(self, post):
        # Get the link's hash (for that is the unique key)
        link_code = VerifyUnique.__get_hash(post.link)

        file_name = self.serialized_objects_path + link_code

        VerifyUnique.__serialize_post(file_name, post)

    @staticmethod
    def __get_hash(text):
        import hashlib
        hash_object = hashlib.md5(text)
        return hash_object.hexdigest()

    @staticmethod
    def __deserialize_post(file_name):
        import pickle
        with open(file_name, 'rb') as inf:
            post = pickle.load(inf)

        return post

    @staticmethod
    def __serialize_post(file_name, post):
        import pickle
        # os.remove(file_name)
        with open(file_name, 'wb') as outf:
            pickle.dump(post, outf)

# for testing purpose

host = 'https://www.leetcode.com/'
link = 'https://www.leetcode.com/problems/add-digits/'
# file_name1 = r'/Users/anupamjain/code/gitRepo/Questions/Algo/python/BullsAndCows.py'
file_name2 = r'/Users/anupamjain/code/gitRepo/Questions/Algo/Java/AddDigits.java'
post = Post(host_name=host, link=link, file_name=file_name2)
config = ConfigParser.ConfigParser()
config.read('config.cfg')
verifier = VerifyUnique(config)
print verifier.check_post_exists(post)
