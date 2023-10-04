import time

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

start = time.time()
ask_user()
complex_math_calculation()
print(f'Single thread took {time.time() - start} time to complete.')

a = 2.162187099456787
b = 5.47699761390686 
c = a + b
d = 7.640185356140137
print(c, '          ' , d)