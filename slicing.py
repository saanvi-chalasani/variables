Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[8:]
''
>>> code[4:]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    code[4:]
NameError: name 'code' is not defined. Did you forget to import 'code'?
>>> a[4:]
'gnan'
>>> a="work until you succed"
>>> a[6:11]
'ntil '
>>> a[5:11]
'until '
>>> a[0:5]
'work '
>>> a[13:16]
'u s'
>>> a[12:15]
'ou '
>>> a[11:15]
'you '
>>> a="codegnan it solutions"
>>> a="I am learning python"

>>> a[-16:-7]
' learning'
>>> a[[-7:-1]
...   
SyntaxError: invalid syntax
>>> a[-7:-1]
...   
' pytho'
>>> a[-7:0]
...   
''
>>> a[-7:]
...   
' python'
