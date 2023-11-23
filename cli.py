"""
CLI to call Lilypond to typeset music from a file, then keep only the cropped image.
"""

import argparse
import logging
import os
import subprocess
from typing import List


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def run_and_log(commands: List[str]):
    commands_str = ' '.join(commands)
    logger.info(f'Running command: {commands_str}')
    subprocess.run(commands)


def remove_uncropped_rename_cropped(filepath: str, extension: str):
    """Lilypond seems to have no way of outputting only cropped image.
    
    So let's delete the uncropped image then rename the cropped one,
    if both are present.
    """
    filepath_uncropped = filepath.replace('.ly', extension)
    filepath_cropped = filepath.replace('.ly', f'.cropped{extension}')
    if os.path.exists(filepath_uncropped) and os.path.exists(filepath_cropped):
        logger.info(f"Removing {filepath_uncropped}")
        os.remove(filepath_uncropped)
        logger.info(f"Renaming {filepath_cropped} -> {filepath_uncropped}")
        os.rename(filepath_cropped, filepath_uncropped)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    parser.add_argument('-p', '--png', action='store_true', help='Output PNG')
    parser.add_argument('-s', '--svg', action='store_true', help='Output SVG')
    args = parser.parse_args()

    # TODO: resolution as argument?
    dpi = 500

    filepath = args.filepath
    _, extension = os.path.splitext(filepath)
    if extension != ".ly":
        raise RuntimeError(f"Filepath extension must be .ly (Lilypond). Invalid filepath: {filepath}")

    folder, _ = os.path.split(filepath)
    
    if args.png:
        run_and_log(['lilypond', f'--output={folder}', '--png', f'-dresolution={dpi}', filepath])
        remove_uncropped_rename_cropped(filepath, '.png')
    
    if args.svg:
        run_and_log(['lilypond', f'--output={folder}', '--svg', filepath])
        remove_uncropped_rename_cropped(filepath, '.svg')
    
    if not args.png and not args.svg:
        logger.warn("Please specify -p and/or -s options else nothing will happen!")

if __name__ == "__main__":
    cli()
