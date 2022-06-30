#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import clipboard

def main(argv):
    ap = argparse.ArgumentParser()
    sup = ap.add_subparsers()
    ap_lower = sup.add_parser('lower', aliases=['l'])
    ap_lower.set_defaults(_process=str.lower)
    args = ap.parse_args(argv[1:])
    text = clipboard.paste()
    text = args._process(text)
    clipboard.copy(text)
    return 0

if __name__ == '__main__':
    print(sys.argv)
    sys.exit(main(sys.argv))
