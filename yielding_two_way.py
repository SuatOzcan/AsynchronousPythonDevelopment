from collections import deque

friends = deque(('Rolf','Jose','Charlie','Jen','Anna'))

def get_friend():
    yield from friends

c = get_friend()
# print(next(c))
# print(next(c))

def greet(g):
        while True:
            try:
                friend = next(g)
                yield f'Hello {friend}!'
            except StopIteration:
                yield 'End of iteration.'

# print(next(greet(get_friend())))

friend_generator = get_friend()
greet_generator = greet(friend_generator)
print(next(greet_generator))
print(next(greet_generator))
print(next(greet_generator))
print(next(greet_generator))
print(next(greet_generator))
print(next(greet_generator))