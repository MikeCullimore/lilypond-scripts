"""
Compile piano scale Lilypond file, using template and separate input file.

todo:
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

def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

template = 'template-piano-scale.ly'
template_inputs = 'template-inputs.ly'

delete_file(template_inputs)

inputs = glob.glob('*.ly')

for input in inputs:
    if input == template:
        print(f'Skipping template: {template}')
        continue
    
    # TODO: copy input to template inputs.
    print(input)
    shutil.copy2(input, template_inputs)
    
    # TODO: call Lilypond (subprocess?)
    # TODO: remove cropped from filename and delete uncropped.

# TODO: remove template inputs.
# delete_file(template_inputs)