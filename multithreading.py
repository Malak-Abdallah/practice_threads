from threading import *
from time import sleep


class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)  # so we don't have a collision


class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


o1 = hello()
o2 = hi()

# after this ==> we have three threads in total
o1.start()
sleep(0.2)
o2.start()

# print("bye") #in this case main thread will print this before the other two thread terminates

# to not ake this happen we join the two threads as we are saying to the main thread to pause its process
# until the two threads terminate.

o1.join()
o2.join()

print("bye")
