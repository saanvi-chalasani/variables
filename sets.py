Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={3,3.5,"python",6+9j,True,False}
print(a)
{False, True, (6+9j), 3.5, 'python', 3}
type(a)
<class 'set'>
a=
SyntaxError: invalid syntax
a={1,2,3,4,5,6,7}
print(a)
{1, 2, 3, 4, 5, 6, 7}
a={1,2,2,3,4,4}
print(a)
{1, 2, 3, 4}
a={1,2,3,4,5,6,7}
b={4,5,6,7}
b.issubset(a)
True
a.issubset(b)
False
a={1,2,3,4,5}
a.add(5)
a
{1, 2, 3, 4, 5}
a={1,2,3,4,5}
b={8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 8, 9, 10}
a.intersection(b)
set()
a={1,2,3,4,5,6}
b={2,3,4,5,6}
a.intersection(b)
{2, 3, 4, 5, 6}
a={5,6,7,8,9,10}
b={9,10,11,12}
a.update(b)
a
{5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{5, 6, 7, 8, 9, 10, 11, 12}
a={4,5,6,7,8}
b={1,2,3,4,5}
a.difeerence(b)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.difeerence(b)
AttributeError: 'set' object has no attribute 'difeerence'. Did you mean: 'difference'?
a.difeerence?(b)
SyntaxError: invalid syntax
a.difference(b)
{8, 6, 7}
b.difference(a)
{1, 2, 3}
={3,4,5,6,7,8}
SyntaxError: invalid syntax
a=={3,4,5,6,7,8}
False
a={3,4,5,6,7,8}
b={6,7,8,9,10}
a.symmetric_difference(b)
{3, 4, 5, 9, 10}
a.difference_update(b)
a
{3, 4, 5}
b.difference_update(a)
b
{6, 7, 8, 9, 10}
a.intersection_update(b)
a
set()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.intersection_update()
a.intersection_update(b)
a
{4, 5, 6}
b.intersection_update(a)
b
{4, 5, 6}
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetricdifference_update(b)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.symmetricdifference_update(b)
AttributeError: 'set' object has no attribute 'symmetricdifference_update'. Did you mean: 'symmetric_difference_update'?

a.symmetric_difference_update(b)
a
{1, 2, 7, 8}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8}
a.copy()
{8, 1, 2, 7}
a={1,2,3,4,5,6}
a.copy()
{1, 2, 3, 4, 5, 6}
a.clear()
a
set()
a.add(3)
a
{3}
a.add(4)
a
{3, 4}
a.pop()
3
a.add(6)
a
{4, 6}
a.remove(4)
a
{6}
a.add(7)
a
{6, 7}
a.add(6)

a
{6, 7}
a.add(9)
a
{6, 7, 9}
a.discard(9)
a
{6, 7}
a.len()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.len()
AttributeError: 'set' object has no attribute 'len'
len(a)
2
a.count()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'

a.count(6)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.count(6)
AttributeError: 'set' object has no attribute 'count'
a.index(8)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.index(8)
AttributeError: 'set' object has no attribute 'index'
>>> a={4,5,6,7,8}
>>> b={7,8,9,2,1}

>>> a.isdisjoint(b)
False
>>> a={1,2,3,4,5}
>>> b={6,,7,8,9}
SyntaxError: invalid syntax
>>> b={6,7,8,9}
>>> a.isdisjoint(b)
True
>>> a=[9,1,5,3,8,4,6,3,7,0]
>>> a1=[9,1,5,3,8]

>>> a
[9, 1, 5, 3, 8, 4, 6, 3, 7, 0]
>>> a1
[9, 1, 5, 3, 8]
>>> a2=[4,6,3,7,0]
>>> a2
[4, 6, 3, 7, 0]
>>> ai.sort()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    ai.sort()
NameError: name 'ai' is not defined. Did you mean: 'a'?
>>> a1.sort()
>>> a2.sort()

>>> a1
[1, 3, 5, 8, 9]
>>> a2
[0, 3, 4, 6, 7]
>>> a2.reverse()
>>> a1.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> a1
[9, 8, 5, 3, 1]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 3, 1]
