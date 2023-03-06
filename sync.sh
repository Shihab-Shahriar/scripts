#!/bin/bash 
remote="khanmd@hpcc.msu.edu"
rsync -azP "$1/" "$remote:~/$1"

# rclone to copy from/to google drive, notice --max-age param
# rclone copy -P --max-age 7d --no-traverse gdrive:reading/ reading/
