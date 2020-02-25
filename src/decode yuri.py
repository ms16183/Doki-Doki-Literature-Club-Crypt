#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
from base64 import b64decode

def main():

    fname = "./yuri.chr"

    if not os.path.exists(fname):
        print("Error: " + fname + " not found.", file=sys.stderr)
        exit(1)

    # yuri.chrの実態はbase64テキスト．
    text = open(fname, "r").read()
    # base64でデコードする．
    print(b64decode(text).decode())


if __name__ == "__main__":
    main()

