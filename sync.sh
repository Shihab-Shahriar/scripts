#!/bin/bash 
remote="khanmd@hpcc.msu.edu"
rsync -azP "$1/" "$remote:~/$1"