# # Provide the number of files to be moved in the command line
# # Example:  python move_random_files.py 21
# # To move 21 jpegs to the folder named 21

import os
import sys
import shutil as sh
import random
from pathlib import Path
import argparse
import logging

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Move a specified number of random JPEG files to a new folder.')
    parser.add_argument('num_files', type=int, help='Number of files to move')
    args = parser.parse_args()
    desired = args.num_files

    # Make a list of jpegs
    files = [f for f in Path('.').iterdir() if f.suffix == '.jpg']

    # Check arguments
    if desired >= len(files):
        logging.error("Can't move more files than there is, bye")
        sys.exit()

    # Make a list of random files to be moved
    to_move = random.sample(files, desired)

    # Create new folder named by the number of files to be moved
    newpath = Path(str(desired))
    newpath.mkdir(exist_ok=True)

    # Now move random files to the folder
    for f in to_move:
        logging.info(f'Moving {f} to {newpath / f.name}')
        sh.move(str(f), newpath / f.name)
    logging.info("Done.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)