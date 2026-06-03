Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list and list methods
a=[3,5,6 "python",8+9j,True, False]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=[3,5.6, "python",8+9j,True, False]
print(a)
[3, 5.6, 'python', (8+9j), True, False]
type(a)
<class 'list'>
b=6.6
type(B)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(B)
NameError: name 'B' is not defined. Did you mean: 'b'?
type(b)
<class 'float'>
a=["python,java,c,]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["python,java,c"]
   
a.append("c++")
   
a
   
['python,java,c', 'c++']
a.extend(["ml" ,"css"])
   
a
   
['python,java,c', 'c++', 'ml', 'css']
a.insert("2,html")
   
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.insert("2,html")
TypeError: insert expected 2 arguments, got 1
a.insert(2,"html")
   
a
   
['python,java,c', 'c++', 'html', 'ml', 'css']
a.index("java")
   
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.index("java")
ValueError: list.index(x): x not in list
a.index("c++")
   
1
a.copy()
   
['python,java,c', 'c++', 'html', 'ml', 'css']
b=a.copy()
   
b
   
['python,java,c', 'c++', 'html', 'ml', 'css']
a.sort()
   
a
   
['c++', 'css', 'html', 'ml', 'python,java,c']
a.reverse()
   
a
   
['python,java,c', 'ml', 'html', 'css', 'c++']
a.pop()
   
'c++'
a
   
['python,java,c', 'ml', 'html', 'css']
a.pop(2)
   
'html'
a
   
['python,java,c', 'ml', 'css']

a.remove
   
<built-in method remove of list object at 0x000001950A7F0100>
a.remove()
   
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a.cleara=["saanvi","pravallika","rishitha"]
   
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.cleara=["saanvi","pravallika","rishitha"]
AttributeError: 'list' object has no attribute 'cleara' and no __dict__ for setting new attributes. Did you mean: 'clear'?
a=["saanvi","pravallika","rishitha"]
   
len(a)
   
3
a.count()
   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count("s")
...    
0
>>> a.cler()
...    
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.cler()
AttributeError: 'list' object has no attribute 'cler'. Did you mean: 'clear'?
>>> a.clear()
...    
>>> a
...    
[]
>>> a.append("saanvi")
...    
>>> a
...    
['saanvi']
>>> #tuple
...    
>>> a=(5,8.9,"saanvi",8+9j,True,False)
...    
>>> print(a)
...    
(5, 8.9, 'saanvi', (8+9j), True, False)
>>> type(a)
...    
<class 'tuple'>
>>> len(a)
...    
6
>>> a.count("saanvi")
...    
1
>>> a=[9,1,5,2,8,4,6,3,7,0]
...    
>>> a.sort()
...    
>>> a
...    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.insert(1,7)
...    
>>> a
...    
[0, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9]
