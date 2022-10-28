"""
lilypond.py

http://lilypond.org/text-input.html

todo:
Is there any advantage to doing this via Python? Just create Lilypond inputs in a text editor and call directly.
Generate images of all piano scales in Trinity book, with fingering, over two octaves (or more as required). 
Use tablature.
Synchronise with guitar neck images and animate.
    For longer pieces, scroll horizontally.
    Highlight current note(s) in different colour?
Fix PNG output.
    Works when calling lilypond directly at the command line.
    Fails even when input file is in current folder.
    Fails with both os.system and subprocess.run.
    Convert a working format (PDF, SVG) to PNG by another means?
        GIMP? https://www.gimp.org/docs/python/index.html
        Could also be useful for other image manipulation tasks later on (e.g. compositing frames).
    Example error:
        GNU LilyPond 2.22.2
        Processing `data/test.ly'
        Parsing...
        Interpreting music...
        Preprocessing graphical objects...
        Finding the ideal number of pages...
        Fitting music on 1 page...
        Drawing systems...
        Converting to PNG...
        warning: `(gs -q -dNODISPLAY -dNOSAFER -dNOPAUSE -dBATCH -dAutoRotatePages=/None -dPrinted=false /tmp/lilypond-tmp-830687)' failed (32512)
Use abjad or just create text input directly? https://pypi.org/project/abjad/
"""

import inspect
import os.path
import subprocess

folder = 'data'

def get_filepath(filename, folder='data'):
    return os.path.join(folder, filename)

def call_lilypond(input, filename):
    """Save Lilypond input to file."""
    # text = inspect.cleandoc("""
    #     \\version "2.22.2"
    #     {    
    #         c' e' g' e'
    #     }""")
    text = f'\\version "2.22.2" {{ {input} }}'
    filepath = get_filepath(filename)
    # with open(filepath, 'w') as f:
    #     f.write(text)
    
    # Pass file to Lilypond with desired args.
    format = 'svg'  # works
    # format = 'png'  # fails
    commands = ['lilypond', f'--format={format}', f'--output={folder}', filepath]
    completed_process = subprocess.run(commands)
    # print(completed_process.stdout)
    # print(completed_process.stderr)#

def test():
    call_lilypond("c' e' g' e'", 'test2.ly')

def c_major_scale():
    call_lilypond("c' d' e' f' g' a' b' c'", 'C_major_scale.ly')

def main():
    # test()
    c_major_scale()

if __name__ == '__main__':
    main()
