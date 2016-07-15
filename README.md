# python2-python3-syntax-updator
Takes a python2 module and automatically makes it python3 compatible.

This function already exists with `2to3 -w your_python_file.py.`  This repository was just for giggles.

# Usage
`python update_print.py`

With no arguments, it will go through all '\*.py' files in a directory, 
and relpace all instances of `print 'something'` with `print('something')`.
Arguments that can be used are `--file` for fixing up an individual file, 
and `--dir` for fixing up a specified directory.

To double-check everything has been changed, one could run:
`grep -rnw '.' -e "print "` in a linux terminal.

# Alternatives
To fix up files in more ways than just the 'print' function, run
`2to3 -n -w .`
in the directory of a python project.
