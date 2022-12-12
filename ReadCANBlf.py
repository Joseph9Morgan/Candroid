import can
import time
import os
from argparse import ArgumentParser, Namespace


def read_blf_file(filename):
    # filename = "2022-11-09-16-19-09.blf"
    can_log = can.BLFReader(filename)
    for msg in can_log:
        print(msg)


def save_blf_file_txt(filename, txtname):
    command = 'python %s %s' % (os.path.abspath(filename),os.path.abspath(txtname))
    os.system(command)
    # filename = "2022-11-09-16-19-09.blf"
    can_log = can.BLFReader(filename)
    for msg in can_log:
        print(msg)


def main(args:Namespace):


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('--i', default=False, action = 'store_true')
    read_blf_file("2022-11-09-16-19-09.blf")


# read and output into terminal
# save he result into a .txt file     >output.txt          
# argparser inputfile outfilename
