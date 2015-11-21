"""
Parse the given page of leetcode.com to get the problem description.
"""
from bs4 import BeautifulSoup
from bs4 import element


def parse_for_post(text):
    soup = BeautifulSoup(text, 'html.parser')
    lst = soup.find_all('div', class_="question-content")
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
                p_list = content.contents
                for p in p_list:
                    if type(p) is element.Tag:
                        '''
                        print p
                        print ' : '
                        '''
                        if 'Credits:' in p.text:
                            continue
                        if p.id == 'hints':
                            # print("inside if")
                            for li in p.contents:
                                if 'class' in li.attrs and li['class'] is 'hint':
                                    del li['class']
                        '''
                        print p.text

                        print '---------------------'
                        '''
                        result_tag.append(p)

                '''print ' : '
                print content
                print ' : '
                print content.text

                print '================'
                '''
                break

            # print '================'
        # print '================'

    # print result_tag
    return result_tag
