#!/usr/bin/env python
import sys
from argparse import ArgumentParser


def main():
    ap = ArgumentParser()
    ap.add_argument('--debug', action='store_true')
    ap.add_argument('others', nargs='*')
    args = ap.parse_args()

    print >>sys.stderr, 'SYS ARGV', sys.argv
    print 'ARGS', args

if __name__ == '__main__':
    sys.exit(main())
