"""Givena  project, find number of files and LOC count for each language to estimate project size. Counts comments."""

import os, sys


def get_loc(fpath):
    ans  = 0
    with open(fpath) as fh:
        for line in fh.readlines():
            if line.strip():
                ans += 1
    return ans



ROOT = os.getcwd()
if len(sys.argv)>1:
    ROOT = sys.argv[1]
print(f"{ROOT=}")

formats = ['py', 'c', 'cpp', 'java']
loc = {f:0 for f in formats}
nfiles = {f:0 for f in formats}

for dirpath, dirs, files in os.walk(ROOT):
    for f in files:
        format_ = f.split('.')[-1]
        #print(f,format_)
        if format_ in formats:
            nfiles[format_] += 1
            loc[format_] += get_loc(os.path.join(dirpath, f))


for f in formats:
    if nfiles[f]:
        print(f, nfiles[f], loc[f])
        print()