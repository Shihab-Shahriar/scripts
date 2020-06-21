import time
import psutil
from multiprocessing import Process, SimpleQueue
import signal, sys
import matplotlib.pyplot as plt


def monitor(q):
    i = 0
    avg, mx, vs = 0,0,[]
    favg, fmx, fvs = 0,0,[]
    while q.empty():
        i += 1
        temps = psutil.sensors_temperatures()   
        fan = psutil.sensors_fans()['nct6798'][1].current
        for t in temps['k10temp']:
            if t.label=="Tdie":
                break
                
        mx = max(mx,t.current)
        avg = ((i-1)*avg+t.current)/i
        vs.append(t.current)
        
        fmx = max(fmx,fan)
        favg = ((i-1)*favg+fan)/i
        fvs.append(fan)
        
        print(f"Tdie cur:{t.current:.2f}, avg:{avg:.2f}, max:{mx:.2f}",end='')
        print(f"\tFan  cur:{fan:.2f}, avg:{favg:.2f}, max:{fmx:.2f}\r",end='')

        time.sleep(1.0)
    print()
        
    plt.subplot(1,2,1)
    plt.title("CPU temp")
    plt.ylim(25,90)
    plt.plot(range(len(vs)),vs);
    
    plt.subplot(1,2,2)
    plt.title("Fan speed")
    plt.ylim(500,3500)
    plt.plot(range(len(vs)),fvs);

    plt.savefig(sys.argv[1]+".png")
    plt.show();


def benchmark(func):
    q = SimpleQueue()
    p = Process(target=monitor,args=(q,))
    p.start()
    s = time.perf_counter()
    func()
    e = time.perf_counter()
    print(f"\nTook {e-s:.2f} secs")
    q.put('boo')
    p.join()
        