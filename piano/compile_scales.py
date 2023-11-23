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
    print(f"Found {len(inputs)} files.")

    template = 'template-piano-scale.ly'
    template_inputs = 'template-inputs.ly'
    commands = ['lilypond', '--svg', f'--output={folder}', '-dno-point-and-click', template]

    for input in inputs:
        print(f'Input: {input}')
        
        # Copy input to template inputs.
        print(f'Copy: {input} to {template_inputs}')
        shutil.copy2(input, template_inputs)
        
        # Compile via Lilypond.
        print(f"Running commands: {commands}")
        subprocess.run(commands)

        # Remove cropped from filename and delete uncropped.
        svg = input.replace('.ly', '.svg')
        cropped = svg.replace('.svg', '.cropped.svg')
        print(f"Deleting {svg}")
        delete_file(svg)
        print(f"Renaming {cropped} to {svg}")
        shutil.move(cropped, svg)

def find_lilypond_files(folder):
    return glob.glob(os.path.join(folder, '**/*.ly'), recursive=True)

def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

# delete_file(template_inputs)

if __name__ == '__main__':
    main()