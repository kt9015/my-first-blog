# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import math


times = [0 for i in range(100)]
sinxs = [0 for i in range(100)]

time = 0
sinx = 0

# initialize matplotlib
plt.ion()
plt.figure()
li, = plt.plot(times, sinxs)

plt.ylim(-1,1)
plt.xlabel("time")
plt.ylabel("sin")
plt.title("sin real time plot")

while 1 :

    time += 0.1
    sinx = math.sin(time)

    times.append(time)
    times.pop(0)
    sinxs.append(sinx)
    sinxs.pop(0)

    li.set_xdata(times)
    li.set_ydata(sinxs)
    plt.xlim(min(times), max(times))
    plt.draw()

    plt.pause(0.01)