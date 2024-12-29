# Provide the number of files to be moved in the command line
# Example:  python move_random_files.py 21
# To move 21 jpegs to the folder named 21

import os
import sys
import shutil as sh
import random

desired:int = 0
if len(sys.argv) > 1:
    desired:int = int(sys.argv[1])
else:
    print("Nothing to do, bye")
    sys.exit()

# Make a list of jpegs
files = []
files += [f for f in os.listdir() if f.endswith('.jpg')]

# Check arguments
if (desired >= len(files)):
    print("Can't move more files than there is, bye")
    sys.exit()

# Make a random list of files to be moved
to_move = random.sample(range(0, len(files)), desired)

# Create new folder named by the number of files to be moved
newpath = str(desired)
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Now move random files to the folder
for f in to_move:
    print(files[f])
    sh.move (files[f], f'{newpath}\\{files[f]}')
print("Done.")