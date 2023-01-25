import os,sys

"No of files for each folder under given dir"

root = "."
if len(sys.argv)>1:
    root = sys.argv[1] 

dirs = next(os.walk(root))[1]
print(len(dirs))

for d in dirs:
    print(d)
    os.system(f"find {root}/{d}/ -type f| wc -l")
    print()
