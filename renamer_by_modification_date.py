import os
from os import path
import time

""" MyFile class 

 This is a class to manage files which are being sorted

"""


class MyFile():

    def __init__(self, filename_p, mtime_p):
        self.filename = filename_p
        self.mtime = mtime_p


def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    files = []

    for filename in os.listdir(folder):
        if (path.isfile(filename) and str(filename) != __file__):
            files.append(MyFile(filename, time.ctime(path.getmtime(filename))))

    files.sort(key=lambda x: x.mtime, reverse=False)

    print "*" * 20
    print "Files has been sorted !"
    print "*" * 20

    for i, current_file in enumerate(files):
        print 'Previous name: %s' % str(current_file.filename)
        os.rename(current_file.filename, '%i - %s' % (i, str(current_file.filename)))
        print 'Current name: ' + str(i) + " - " + str(current_file.filename)


if __name__ == "__main__":
    main()
