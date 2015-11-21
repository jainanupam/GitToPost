"""
Prepare the post file.
"""
import os.path
from parser.codeParser import CodeParser

output_dir = r'/Users/anupamjain/code/gitRepo/GitToPost/posts/'


def make_post(file_name, problem_text):
    """
    prepare and save the post file.

    :param file_name: source code file
    :param problem_text: problem description
    :return:
    """
    base_name = os.path.basename(file_name)
    name = os.path.splitext(base_name)[0]
    code_parser = CodeParser()
    code = code_parser.get_code(file_name)
    with open(output_dir + name, 'w') as outf:
        outf.write(str(problem_text))
        outf.write('\n----------------\n')
        outf.write('<pre class="lang:java decode:true ">')
        outf.write(code)
        outf.write('</pre>')

