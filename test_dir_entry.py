#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
from directory_entry import directory_entry
x = directory_entry(pathname="/Users/erik/videoportrait")
x.find_children()
x.print_children(filetype='python')
