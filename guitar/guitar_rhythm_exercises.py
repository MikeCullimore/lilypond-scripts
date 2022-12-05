"""
Generate guitar exercise sheet music from given chords and strumming pattern.

todo:
Generate different chords (common four chord progressions in random key?)
Generate different rhythms (discuss with Andrew).
Generalise to other progressions e.g. 12 bar blues.
"""


import os
import shutil
import subprocess

def main():
    inputs_filepath = 'guitar-inputs.ly'
    chords = ['c', 'g', 'a:m', 'f']
    rhythm = [4, 8, 8, 4, 8, 8]
    write_inputs_file(inputs_filepath, chords, rhythm)

    template_filepath = 'guitar-strum-rhythms.ly'
    compile_template(template_filepath)

    cleanup_files(template_filepath)

def compile_template(template):
    subprocess.run(['lilypond', '--svg', template])

def write_inputs_file(filepath, chords, rhythm):
    chords_string = chords_to_string(chords)
    rhythm_string = rhythm_to_string(rhythm)
    with open(filepath, 'w') as f:
        f.writelines([chords_string, '\r\n', rhythm_string])

def chords_to_string(chords):
    chords_string = f'Chords = \chordmode {{ {chords[0]}1'
    for chord in chords[1:]:
        chords_string += f' | {chord}'
    chords_string += ' }'
    print(chords_string)
    return chords_string

def rhythm_to_string(rhythm):
    rhythm_string = 'Rhythm = {'
    for beat in rhythm:
        rhythm_string += f' c{beat}'
    rhythm_string += ' }'
    print(rhythm_string)
    return rhythm_string

def cleanup_files(template_filepath):
    svg = template_filepath.replace('.ly', '.svg')
    cropped = svg.replace('.svg', '.cropped.svg')
    os.remove(svg)
    shutil.copy2(cropped, svg)
    os.remove(cropped)

if __name__ == '__main__':
    main()
