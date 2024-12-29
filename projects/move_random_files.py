import os
import sys
import shutil as sh
import random
all_files = os.listdir()
files = []

# Make a list of jpegs
for f in range(0, len(all_files)):
    if (all_files[f][-4:] == '.jpg'):
        files.append(all_files[f])

desired:int = int(sys.argv[1])

# Check arguments
if desired >= len(files):
    # can't move more files then there is
    print("Nothing to do")
    sys.exit()

# Make a random list files to be moved
to_move = random.sample(range(0, len(files)), desired)

# Create new folder named by the number of files to be moved
newpath = str(desired)
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Now move random files to the folder
for f in to_move:
    print(files[f])
    sh.move (files[f], f'{newpath}\\{files[f]}')