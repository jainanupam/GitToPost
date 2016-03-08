"""
Check whether the current file/link being
checked is unique or if there already is
a file related to this post.
"""
import os
import os.path as path
import shutil
# imports for testing purpose
import ConfigParser
from post import Post


class VerifyUnique(object):
    def __init__(self, config):
        self.__dict__ = {'IS_UNIQUE': 0, 'NEW_CODE': 1, 'NON_UNIQUE': 2}
        parent_out_dir = config.get('Paths', 'output_dir')
        # Get the serialized files which are new and not posted on site
        self.serialized_objects_path = parent_out_dir + 'posts-serial/'
        self.files = set(os.listdir(self.serialized_objects_path))
        self.post_files = set(os.listdir(self.serialized_objects_path))
        # Get the serialized files which are already posted
        self.posted_serialized_objects_path = parent_out_dir + 'posted-serials/'
        self.posted_files = [f for f in os.listdir(self.posted_serialized_objects_path)
                             if path.isfile(path.join(self.posted_serialized_objects_path, f))
                             and f != '.DS_Store']
        #self.posted_files = set(os.listdir(self.posted_serialized_objects_path))

    def check_post_exists(self, post):
        """
        Check whether the given post already exists or not.
        :param post:
        :return:
        """
        # Get the link's hash (for that is the unique key)
        link_code = VerifyUnique.__get_hash(post.link)
        # print 'link hash: ' + link_code

        # Check if the hash exists in the self.post_files or self.posted_files
        # print self.files
        if link_code not in self.post_files \
                and link_code not in self.posted_files:
            # If not exists, serialize this post and return True1
            post.files_covered = set()
            post.files_covered.add(post.file_name)
            return self.IS_UNIQUE

        # If it does, need to unpickle the existing object
        serial_file_path = None
        if link_code in self.posted_files:
            serial_file_path = self.posted_serialized_objects_path
            #file_name = self.posted_serialized_objects_path + link_code
        elif link_code in self.post_files:
            serial_file_path = self.serialized_objects_path
            #file_name = self.serialized_objects_path + link_code

        deserialized_post = VerifyUnique.__deserialize_post(serial_file_path + link_code)

        # print deserialized_post.host_name, deserialized_post.link, \
        #    deserialized_post.file_name, deserialized_post.files_covered

        # Check if the unpickle object has the current code
        # file in it's list. if yes, return False
        if post.file_name in deserialized_post.files_covered:
            return self.NON_UNIQUE

        # print post.file_name
        # If the current code file is not already covered,
        # update the old object with current file.
        deserialized_post.files_covered.add(post.file_name)

        if link_code in self.posted_serialized_objects_path:
            # the file is posted already. Check the post file
            # and move it to un-posted area if required.
            if 'posted' in deserialized_post.post_file:
                new_file_name = VerifyUnique.__remove_posted_dir(deserialized_post.post_file)
                # move the file to new location.
                # TODO Check usage of shutil.move as well.
                os.rename(deserialized_post.post_file, new_file_name)
                # set the new file name in deserialized post
                deserialized_post.post_file = new_file_name
            # remove existing serialized file
            os.remove(serial_file_path + link_code)
            # set the new path for serializing this object
            serial_file_path = self.serialized_objects_path

        VerifyUnique.__serialize_post(serial_file_path + link_code, deserialized_post)

        post.post_file = deserialized_post.post_file

        return self.NEW_CODE
        # Should pickle/ unpickle be included as part of this?
        # (YES)

    def serialize_post(self, post):
        # Get the link's hash (for that is the unique key)
        link_code = VerifyUnique.__get_hash(post.link)

        file_name = self.serialized_objects_path + link_code

        VerifyUnique.__serialize_post(file_name, post)

    def move_posted_files(self):
        posted_serials_list = self.posted_files
        # print posted_serials_list
        for posted_serial_file in posted_serials_list:
            deserialized_post = VerifyUnique.__deserialize_post(self.posted_serialized_objects_path + posted_serial_file)
            print "file name", posted_serial_file
            # print "link: ", deserialized_post.link,
            # print "post file", deserialized_post.post_file
            try:
                existing_file_name = deserialized_post.post_file
            except AttributeError as e:
                print e
                print "removing file: ", posted_serial_file
                os.remove(self.posted_serialized_objects_path + posted_serial_file)
                continue
            if 'posted' not in existing_file_name:
                new_file_name = VerifyUnique.__add_posted_dir(existing_file_name)
                shutil.move(existing_file_name, new_file_name)
                deserialized_post.post_file = new_file_name
                VerifyUnique.__serialize_post(self.posted_serialized_objects_path + posted_serial_file, deserialized_post)

    @staticmethod
    def __remove_posted_dir(file_path):
        index = file_path.index('posted')
        return file_path[0: index] + file_path[index + 7:]

    @staticmethod
    def __add_posted_dir(file_path):
        index = file_path.rfind('/')
        return file_path[0: index] + '/posted' + file_path[index:]

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
        try:
            print post.post_file
        except Exception as e:
            print e

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
