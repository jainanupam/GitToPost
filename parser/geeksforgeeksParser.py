"""
Parse the given page of geeksforgeeks.org to get the title and problem description.
"""

import logging
from bs4 import BeautifulSoup
from bs4 import element
from Logger import Logger


class GeeksForGeeksParser(object):
    logger = Logger.get_logger("GeeksForGeeksParser", logging.DEBUG)
    keywords = ['recommend', 'Solution']

    @staticmethod
    def parse(post):
        GeeksForGeeksParser.logger.debug('parsing in GeeksForGeeks')
        title = GeeksForGeeksParser.parse_for_title(post.raw_page)
        # print title
        post.title = title
        content = GeeksForGeeksParser.parse_for_post(post.raw_page)
        return content

    @staticmethod
    def parse_for_title(text):
        soup = BeautifulSoup(text, 'html.parser')
        lst = soup.find_all('h1', class_="entry-title")
        # print lst
        return lst[0].text

    @staticmethod
    def parse_for_post(text):
        soup = BeautifulSoup(text, 'html.parser')
        lst = soup.find_all('div', class_="entry-content")
        # print lst
        result_tag = element.Tag(name='p')
        for div in lst:
            # print type(div),
            # print ' : '
            # print div.contents
            # print '------------------'
            content_list = div.contents
            # print "printing content list"
            for content in content_list:

                # print type(content)
                # print '================='
                if type(content) is element.Tag:
                    flag = True
                    for keyword in GeeksForGeeksParser.keywords:
                        if keyword in content.text:
                            # print "Keyword found in: " + content.text
                            GeeksForGeeksParser.logger.info('keyword found in: ' + content.text)
                            flag = False
                            break
                    if flag:
                        ''' Check if the end keyword has not been found.'''
                        result_tag.append(content)
                    else:
                        ''' End keyword found. End adding new content in post. '''
                        break
                    # print ' : '
                    # print content
                    # print ' : '
                    # print content.text

                    # print '================'

                    # break

                # print '================'
            # print '================'

        # print result_tag
        return result_tag


# For testing purpose
def main():
    from Fetcher import Fetcher
    from post import Post

    link = r'http://www.geeksforgeeks.org/find-xor-of-two-number-without-using-xor-operator/'
    fetcher = Fetcher(logging.DEBUG)
    host, response = fetcher.fetch(link.strip())

    post = Post(link=link, host_name=host, raw_page=response)

    content = GeeksForGeeksParser.parse(post)
    print "===== back to main method ====="
    print content

if __name__ == "__main__":
    main()
