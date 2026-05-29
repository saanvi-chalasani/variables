Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
a=9
b=8
print(a+b)
17
print(a-b)
1
print(a*b)
72
print(a//b)
1
print(a/b)
1.125
print(a**b)
43046721
a=3
b=6
a+=b
a
9
a-=b
a
3
a*=b
a
18
a//=b
a
3
a/=b
a
0.5
a**=b
a
0.015625
a=8
b=6
b+=a
b
14
b-=a
b
6
b/=a
b
0.75
b//=a
b
0.0
b**=a
b
0.0
b*=A
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b*=A
NameError: name 'A' is not defined. Did you mean: 'a'?

b
0.0
#operators
#arthimetic
#comparison
a=9
b=5
a<b
False
b>a
False
a<=b
False
a>=b
True
a==b
False
a!=b
True
#logical
a=6
b=9
a<b and a>b
False
aa<b and b>a
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    aa<b and b>a
NameError: name 'aa' is not defined. Did you mean: 'a'?
a<b and b>a
True
a<=v and a>b
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a<=v and a>b
NameError: name 'v' is not defined
a<=v and b>a
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a<=v and b>a
NameError: name 'v' is not defined
a<=b and b>
SyntaxError: invalid syntax
a<=b and b>a
True
a,b or b.a
(6, 9)
a<b or a>b
True
a<b not a>b
SyntaxError: invalid syntax
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not Treu
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    not Treu
NameError: name 'Treu' is not defined
>>> not True
False
>>> a=9
>>> a=9
>>> a="saanvi"
>>> if(a) is int
SyntaxError: expected ':'
>>> if (a) is str:
...     print("yes it is")
... 
...     
>>> if type(a)is str;
SyntaxError: invalid syntax
>>> if type(a) is str:
...     print("yes it is)
...           
SyntaxError: unterminated string literal (detected at line 2)
>>> print("yes")
...           
yes
>>> #membership
...           
>>> a=123456789
...           
>>> del a
...           
>>> a=1,2,3,4,5,6,7,8,9
...           
>>> if 3 in a:
...           print(3)
... 
...           
3
>>> if 10 not  in a:
...           print(10)
... 
...           
10
