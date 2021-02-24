import datetime as dt
import time

p = "/home/shihab/Downloads/His Dark Materials/s2e3.srt"
delay = 84


s = open(p).read()
subs = s.split("\n\n")

d = dt.datetime(1999,11,20)

def add(t):
    h,m,s = t.split(':')
    secs = 3600*int(h)+60*int(m)+int(s)
    return time.strftime('%H:%M:%S', time.gmtime(secs+delay))


for i in range(len(subs)-1):
    a = subs[i]
    comps = a.split("\n")
    ls, rs = comps[1].split(" --> ")
    ls, lms = ls.split(',')
    rs, rms = rs.split(',')
    ls, rs = add(ls), add(rs)

    comps[1] = f"{ls},{lms} --> {rs},{rms}"
    subs[i] = '\n'.join(comps)

s = '\n\n'.join(subs)
with open("/home/shihab/Downloads/His Dark Materials/dummy.srt","w") as fh:
    fh.write(s)
