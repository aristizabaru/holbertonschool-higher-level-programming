# 0x0C. Python - Almost a circle

## About

This is an educational project to explore several conceptos bout Python

## Topics

-  Import
-  Exceptions
-  Class
-  Private attribute
-  Getter/Setter
-  Class method
-  Static method
-  Inheritance
-  Unittest
-  Read/Write file
-  `args` and `kwargs`
-  Serialization/Deserialization
-  JSON

## Requirements

-  python3 (version 3.4.3)
-  PEP 8 (version 1.7.\*)

## Requirements

Read or watch:

-  [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
-  [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
-  [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
-  [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## File Descriptions

This project is conceived to be carried out step by step, that is why the description of the files is presented as a statement

### 0. If it's not tested it doesn't work

**[0-read_file.py](00-read_file.py)**

All your files, classes and methods must be unit tested and be PEP 8 validated.
_Note that this is just an example. The number of tests you create can be different from the above example._

```
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
```

### 1. Base class

**[0-read_file.py](00-read_file.py)**

Write the first class `Base`:

Create a folder named `models` with an empty file `\__init\__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py`:

-  Class `Base`: - private class attribute `\__b_objects = 0` - class constructor: `def \__init\__(self, id=None):`: - if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it - otherwise, increment `\__nb_objects` and assign the new value to the public instance attribute `id`
   This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$
```
