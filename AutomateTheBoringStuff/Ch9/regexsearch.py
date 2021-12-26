from os import linesep
from pathlib import Path
from typing import Match
p = Path('/home/moit/Desktop')

match = input("Enter a regular expression: ")
print('\n')

for txtfilepath in p.glob('*.txt'):
    f=open(txtfilepath)
    content=f.readlines()
    for line in content:
        if match in line:
            print(line,'This is a line from the file',txtfilepath)