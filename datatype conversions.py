Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datetype inversions
int(900)
900
int(9.0)
9
int("print")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("print")
ValueError: invalid literal for int() with base 10: 'print'
int(7+8j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(7+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(90)
90.0
float(9.0)
9.0
float(saanvi)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(saanvi)
NameError: name 'saanvi' is not defined
float(9=8j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
float(Treu)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(Treu)
NameError: name 'Treu' is not defined
float(True)
1.0
float(False)
0.0
str(9)
'9'
str(9.0)
'9.0'
>>> str(saanvi)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str(saanvi)
NameError: name 'saanvi' is not defined
>>> str("saanvi")
'saanvi'
>>> str(9.8j)
'9.8j'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(9)
(9+0j)
>>> complex(9.9j)
9.9j
>>> comple(9.8)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    comple(9.8)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(9.0)
(9+0j)
>>> complex("saanvi")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("saanvi")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(90)
True
>>> bool(9.0)
True
>>> bool("saanvi")
True
>>> bool(9+9j)
True
>>> bool(True)
True

>>> bool(False)
False
