import time
import itertools
import threading
import sys

done = False

def animate():
    for c in itertools.cycle(['11', '10', '9', '8', '7', '6', '5', '4', '3', '12', '1']):
        if done:
            break
        sys.stdout.write('\rAbout has close in seconds. ' + c)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(10.8)
done = True
print("")
