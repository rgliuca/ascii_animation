import time
t1 = []
t2 = []

for i in range(10):
    t1.append(time.time())
    time.sleep(0.001)
    t2.append(time.time())

for i in range(10):
    print(t1[i],t2[i], t2[i]-t1[i])
