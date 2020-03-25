"""
Deque

-uma lista de alta performance

"""
from collections import deque

# adiciona elementos no começo ou no final da lista
d = deque('isabela')
print(d)
d.append('y')  # deque(['i', 's', 'a', 'b', 'e', 'l', 'a', 'y'])
print(d)
d.appendleft('x')  # deque(['x', 'i', 's', 'a', 'b', 'e', 'l', 'a', 'y'])
print(d)
# remove elementos no começo ou no final da lista
d.pop()
print(d)  # deque(['x', 'i', 's', 'a', 'b', 'e', 'l', 'a'])
d.popleft()
print(d)  # deque(['i', 's', 'a', 'b', 'e', 'l', 'a'])
