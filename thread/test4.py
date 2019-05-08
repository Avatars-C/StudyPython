# -*- coding: utf-8 -*-

import threading
import time

def work(number):
    print("work")
    time.sleep(number)
    return

for i in range(4):
    t=threading.Thread(target=work,args=(i,))
    t.start()