"""
Prepare the post file.
"""
import os.path
from parser.codeParser import CodeParser

default_out_dir = r'/Users/anupamjain/code/gitRepo/GitToPost/posts/'


def make_post(file_name, post, output_dir=default_out_dir):
    """
    prepare and save the post file.

    :param file_name: source code file
    :param post: the post object
    :param output_dir: directory to create the post file into
    :return:
    """

    base_name = os.path.basename(file_name)
    name = os.path.splitext(base_name)[0]
    code_parser = CodeParser()
    code = code_parser.get_code(file_name)
    with open(output_dir + name, 'wb') as outf:
        outf.write("<b>Title: </b>" + post.title)
        outf.write("  <b>Source: </b><a target='_blank' href='" + post.link + "'>" + post.host_name +"</a>")
        outf.write(str(post.problem_text))
        outf.write('\n\n')
        if '.java' in file_name:
            outf.write("<h3>Java solution</h3>")
            outf.write('<pre class="lang:java decode:true ">')
        elif '.py' in file_name:
            outf.write("<h3>Python solution</h3>")
            outf.write('<pre class="lang:python decode:true ">')
        outf.write(code)
        outf.write('</pre>')

