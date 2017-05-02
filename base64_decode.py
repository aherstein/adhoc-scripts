#!/usr/bin/python

from base64 import b64decode

out = open("base64_output.txt", "w+")

with open("base64_input.txt") as f:
    for line in f:
        out.write(b64decode(line))
