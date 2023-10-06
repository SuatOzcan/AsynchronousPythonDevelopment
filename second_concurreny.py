import time
from concurrent.futures import ThreadPoolExecutor

def ask_user():
    start = time.time()
    user_input = input('Please enter your name: ') #This a blocking operation. ur code waits for something to happen.
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user function took {time.time() - start} time to complete.')

def complex_math_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000001)]
    print(f'complex_math_calculation function took {time.time() - start} time to complete.')

with ThreadPoolExecutor(max_workers=2) as pool: #Create 2 threads in this collectionof threads.
    pass
    pool.submit(complex_math_calculation)
    pool.submit(ask_user)


# pool.shutdown() If ThreadPoolExecutor is not used with a "with", it is closed this way.    