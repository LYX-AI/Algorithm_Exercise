# Data structure
'''
List
Ordered collection of items
Mutable(elements)
allows duplicates
my_list=[1,2,3]

Tuples:
Ordered collection of items
Immutable (elements cannot be changed).
Allows duplicates.
my_tuple=(1,2,3)

Set:
Unordered collection of unique items.
Mutable (elements can be added or removed).
Does not allow duplicates.
Example: my_set = {1, 2, 3}

Dictionaries:
Unordered collection of key-value pairs.
Mutable (values can be changed).
Keys must be unique.
Example: my_dict = {'key1': 'value1', 'key2': 'value2'}

Strings:
Ordered collection of characters.
Immutable (characters cannot be changed).
Example: my_string = "Hello"

Arrays (from array module):
Homogeneous collection of items (items must be of the same type).
More memory efficient than lists for large datasets.
Example: import array; my_array = array.array('i', [1, 2, 3])
'''

# k=1000
# i=0
# while k>1:
#     k/=2
#     i+=1
# print(i)

#5.1.1. Using Lists as Stacks
from typing import Collection, Sequence


stack=[3,4,5]
stack.append(6)
print(stack)
print(stack.pop())
print(stack)

# Using List as Queues
from collections import deque
queue=deque(["Eric","John","Micheal"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.pop())
print(queue.popleft())
print(queue)

#List Comprehensions
Sequence=[x**2 for x in range(10)]
print(Sequence)

print([(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y])
#same as 
# combs=[]
# for x in [1,2,3]:
#     for y in [3,4,1]:
#         if x!=y:
#             combs.append((x,y))

vec=[-4,-2,0,2,4]
print([abs(x) for x in vec])

freshfruit=[' banana',' loganberry',' passion fruit']
print([x.strip() for x in freshfruit])

#flatten a list using a listcomp with two 'for':
vec=[[1,2,3],[4,5,6],[7,8,9]]
print([num for element in vec for num in element])

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],]
print([[row[i] for row in matrix] for i in range(4)])

transposed=[]
for i in range(4):
    transposed.append(row[i]for row in matrix)

# same as
transposed=[]
for i in range(4):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(list(zip(*matrix)))

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)



print("--Tuples and Sequences--")
t=12345 ,54321, "Hello"
print(t[0])
print(t)

a=["a"," ","3"," "]
del a[" "]
print(a)