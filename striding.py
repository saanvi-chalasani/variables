Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a[::3]
'dacn'
b=""cloud computing"
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> b="cloud computing"
>>> a[::4]
'd e'
>>> a[::3]
'dacn'
>>> b[::6]
'cci'
>>> b[3:6]
'ud '
>>> b[:9]
'cloud com'
>>> b[7:]
'omputing'
>>> b[::3]
'cucpi'
>>> b[::4]
'cdmi'
>>> a="machine learning"
>>> a[1:10:3]
'ai '
>>> a[2:14:4]
'cea'
>>> a[3:15:5]
'hli'
>>> a{1:12:2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a[1:12:2]
'ahn er'
>>> a="python course"
>>> a[-1:-6:-2]
'ero'
>>> a="python course"
>>> a[-1:-11:-4]
'eoo'
>>> a[-3:-13:-5]
'rn'
>>> a[-5:-12:-6]
'ot'
>>> a[-2:-9:-1]
'sruoc n'
>>> a[-6:-13:-3]
'coy'
>>> a[-4:-12:-6]
'uh'
