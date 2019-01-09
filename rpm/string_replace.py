#!/usr/bin/env python3

import sys
import os
import pystache

lines=open(sys.argv[1]).read()
out_file = open(os.path.splitext(sys.argv[1])[0], "w")
tags = {}
args = sys.argv[2:]
while len(args) > 0:
    key = args.pop(0)
    tags[key] = args.pop(0)

lines = pystache.render(lines, tags)

out_file.write(lines)
out_file.close()

