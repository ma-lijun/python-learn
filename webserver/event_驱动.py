import threading
import time

def producer():
    print(u"chef:等人买包子")
    event.wait()
    event.clear()
    print("开始做包子")
    time.sleep(3)
    print("包子好了")
    event.set()

def consumer():
    print("zs:我去买包子")
    event.set()
    time.sleep(2)
    print("等着包子做好")
    event.wait()
    print("Thinks")


event = threading.Event()
c1 = threading.Thread(target=consumer)
p1 = threading.Thread(target=producer)
p1.start()
c1.start()