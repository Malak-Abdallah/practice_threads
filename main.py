'''
import time
import threading

def myfunc(name):
    print(f'my function started with {name}')
    time.sleep(10)
    print('my function ended')

if __name__ == '__main__':
    print('main started')
    t=threading.Thread(target=myfunc,args=['realpython'])
    t.start()
   # myfunc('realpython')
    print('main ended')
    '''
# import module
from threading import *
import time


# creating a function
def thread_1(seconds):
    for i in range(5):
        print('this is non-daemon thread')
        time.sleep(seconds)


# creating a thread T
T = Thread(target=thread_1, args=[2])

# starting of thread T
T.start()

# main thread stop execution till 5 sec.
time.sleep(5)
print('main Thread execution')

# in this example we are not using join(), so main thread will collise with non-deamon thread.
