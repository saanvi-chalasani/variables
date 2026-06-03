Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print("a+ " " +b")
a+  +b
print(a+ " "+b)
python course
fname="pooja"
lname"ch"
SyntaxError: invalid syntax
lname="ch"
print(fname+lname")
      
SyntaxError: unterminated string literal (detected at line 1)
print(fname+ " " =lname)
      
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print(fname+ " " +lname)
      
pooja ch
print((fname+ " " +lname).title())
      
Pooja Ch
\
>>> #format method
...       
>>> a="saanvi"
...       
>>> b="pravallika"
...       
>>> print("hello {}{}".format(a+b))
...       
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print("hello {}{}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("hello {}{}".format(a,b))
...       
hello saanvipravallika
>>> print("hello {} {}".format(a,b))
...       
hello saanvi pravallika
>>> print("hello{} hello{}".format(a,b))
...       
hellosaanvi hellopravallika
>>> print("hello{} hello{}".format(a+b).title())
...       
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("hello{} hello{}".format(a+b).title())
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("hello{} hello{}".format(a,b).title())
...       
Hellosaanvi Hellopravallika
>>> print("hello {} hello {}".format(a,b).title())
...       
Hello Saanvi Hello Pravallika
>>> #fstring
...       
>>> a="mickey"
...       
>>> b="mouse"
...       
>>> print(f"hello{a} {b}")
...       
hellomickey mouse
>>> print(f"hello {a} {b}".title())
...       
Hello Mickey Mouse
