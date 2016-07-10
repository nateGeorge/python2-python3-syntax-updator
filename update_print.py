from glob import glob
import argparse
import re

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=False, help="Path to the file")
ap.add_argument("-d", "--dir", required=False, help="Directory of file")
args = vars(ap.parse_args())

# looking for python 2 print commands that need to be updated
if args['file'] is not None:
    files = [args['file']]
elif args['dir'] is not None:
    if dir[-1] != '/':
        dir.append('/')
    files = glob(dir + '*.py')
else:
    files = glob('*.py')

changedLine = False
for file in files:
    print('updating:', file)
    with open(file, 'r', encoding = 'ISO-8859-1') as rFile:
        lines = rFile.readlines()
        newLines = []
        newLines.append('from __future__ import print_function\n')
        for line in lines:
            result = re.search(u'([\s*#*]*)print\s+(.+)', line)
            if result is not None:
                newLine = result.group(1) + 'print(' + result.group(2) + ')'
                newLines.append(newLine)
                changedLine = True
            else:
                newLines.append(line)
    if changedLine == True:
        with open(file, 'w') as wFile:
            wFile.writelines(newLines)
