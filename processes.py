import time
#from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

def ask_user():
    start = time.time()
    user_input = input('Please enter your name: ') #This a blocking operation. ur code waits for something to happen.
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user function took {time.time() - start} time to complete.')

def complex_math_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(10000001)]
    print(f'complex_math_calculation function took {time.time() - start} time to complete.')

# start = time.time()
# ask_user()
# complex_math_calculation()
# print(f'Single thread took {time.time() - start} time to complete.')

# process = Process(target=complex_math_calculation)
# process.start()

# start = time.time()

# ask_user()

# process.join()

start = time.time()

with ProcessPoolExecutor(max_workers = 2) as pool:
    pool.submit(complex_math_calculation)
    pool.submit(complex_math_calculation)

print(f'Total time of two processes: {time.time() - start}')
