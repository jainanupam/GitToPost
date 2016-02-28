"""
Prepare the post file.
"""
import os.path
from parser.codeParser import CodeParser

default_out_dir = r'/Users/anupamjain/code/gitRepo/GitToPost/posts/'


def append_to_post(post_file, code_file):
    """
    Method to append code to existing post-file
    :param post_file:
    :param code_file:
    :return:
    """
    code_parser = CodeParser()
    code = code_parser.get_code(code_file)

    with open(post_file, 'a') as outf, open(code_file, 'r') as inf:
        outf.write('<br><br>')
        if '.java' in code_file:
            outf.write("<h3>Java solution</h3>")
            outf.write('<pre class="lang:java decode:true ">')
        elif '.py' in code_file:
            outf.write("<h3>Python solution</h3>")
            outf.write('<pre class="lang:python decode:true ">')
        outf.write(code)
        outf.write('</pre>')


def make_post(file_name, post, output_dir=default_out_dir):
    """
    prepare and save the post file.

    :param file_name: source code file
    :param post: the post object
    :param output_dir: directory to create the post file into
    :return:
    """

    # Get the file name except the file path
    # e.g. /dir/test/file.java --> file.java
    base_name = os.path.basename(file_name)
    # Split the file name base_name into a pair (root, ext)
    name = os.path.splitext(base_name)[0]
    code_parser = CodeParser()
    # get the source code as text from the input file
    code = code_parser.get_code(file_name)
    # Set the output file name into current post object
    post.post_file = output_dir + name
    with open(post.post_file, 'wb') as outf:
        outf.write("<b>Title: </b>" + post.title)
        outf.write("  <b>Source: </b><a target='_blank' href='" + post.link + "'>" + post.host_name + "</a>")
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

