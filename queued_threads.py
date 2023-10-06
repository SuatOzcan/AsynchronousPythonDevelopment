import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() #will be things that e going to be printed out.
counter_queue = queue.Queue() # amounts by which to increase counter.

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() #This waits until an item is available, and then locks the queue.
        old_counter = counter
        counter = old_counter + increment
        job_queue.put(f'New counter value is {counter}', '-------')
        counter_queue.task_done() #This unlocks the counter_queue.