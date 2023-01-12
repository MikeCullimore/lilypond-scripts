"""
Compile piano scale Lilypond file, using template and separate input file.

todo:
Separate the steps specific to piano scales from the general-purpose run Lilypond, rename cropped etc.
Optimise SVG for use with React (why is default not compatible?).
Generalise: (adapt from guitar/guitar_rhythm_exercises.py)
    Handle formatting input to file (function each for piano scale and guitar rhythm exercise).
    Delete template file at end.
    Call Lilypond.
    Delete uncropped image.
    Remove '.cropped' from image filename.
"""

import glob
import os
import shutil
import subprocess

def main():
    folder = 'scales'
    inputs = find_lilypond_files(folder)

    template = 'template-piano-scale.ly'
    template_inputs = 'template-inputs.ly'
    format = 'svg'  # works
    # format = 'png'  # fails
    commands = ['lilypond', f'--format={format}', f'--output={folder}', template]

    for input in inputs:
        print(f'{input}')
        
        # Copy input to template inputs.
        print('Copy to template inputs.')
        shutil.copy2(input, template_inputs)
        
        # Compile via Lilypond.
        print('Compile.')
        subprocess.run(commands)

        # Remove cropped from filename and delete uncropped.
        print('Replace original with cropped.')
        svg = input.replace('.ly', '.svg')
        cropped = svg.replace('.svg', '.cropped.svg')
        delete_file(svg)
        shutil.move(cropped, svg)

def find_lilypond_files(folder):
    return glob.glob(os.path.join(folder, '*.ly'))

def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

# delete_file(template_inputs)

if __name__ == '__main__':
    main()