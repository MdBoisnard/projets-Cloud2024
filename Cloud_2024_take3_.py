Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import turtle as t
>>> from random import random
>>> 
>>> for i in range(100)
SyntaxError: incomplete input
>>> 
>>> for i in range(100) :
...     steps = int(random() * 100)
...     angle = int(random() * 360)
...     t.right(angle)
...     t.fd(steps)
...  for i in range(100) :
...     steps = int(random() * 100)
...     angle = int(random() * 360)
...     t.right(angle)
...     t.fd(steps)


t.mainloop()


