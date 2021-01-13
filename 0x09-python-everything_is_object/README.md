# 0x08. Python - More Classes and Objects

## About

This is an educational project in which a `Rectangle` class is create

## Topics

-  OOP
-  Public, protected and private attributes
-  Special methods
-  Object attribute and a class attribute
-  Object method and a class method

## Requirements

-  Python 3.4
-  pep8 1.7

## File Descriptions

### 0. Simple rectangle

**[0-rectangle.py](0-rectangle.py)**

Write an empty class Rectangle that defines a rectangle.

```
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$
```
