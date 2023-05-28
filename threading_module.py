import threading # calling the threading module
import time # for printing and giving delay in our functions
# Define a function for the thread with the name (print_time) and define two arguments 

def print_time(threadName,delay):
    count = 0 # create a counter and initialize it with 0
    while count < 3: # make a loop and inside it provide a delay (sec) to be
        time.sleep(delay) # able to show the thread execution because the
        count += 1 # execution is fast and it difficult to see it without delay
        print(threadName,"-----------",time.ctime()) #check the thread running
# Create two threads (t1 and t2) which is an objects of thread class :
t1=threading.Thread(target=print_time, args=("Thread 1",1))
t2=threading.Thread(target=print_time, args=("Thread 2",2))
t3=threading.Thread(target=print_time, args=("Thread 3",1))
t4=threading.Thread(target=print_time, args=("Thread 4",3))

# starting thread 1
t1.start()
# starting thread 2
t2.start()
# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()
t3.start()
t3.join()
print("done")



