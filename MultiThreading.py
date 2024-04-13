import threading
import time

def func1():
    for i in range(5):
        print("Talha")

        time.sleep(1)

def func2():
    for i in range(5):
        print("Boss")

        time.sleep(1)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Python")