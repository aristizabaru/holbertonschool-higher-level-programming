# 0x12. JavaScript - Warm up

## About

This is an educational project to explore several conceptos about Javascript.

JavaScript is used for many things, whitin this repocitory, we´ll use JavaScript for 2 reasons:

-  Scripting
-  Web front-end

## Topics

-  Why JavaScript programming is amazing
-  How to run a JavaScript script
-  How to create variables and constants
-  What are differences between `var`, `const` and `let`
-  What are all the data types available in JavaScript
-  How to use the `if`, `if ... else` statements
-  How to use comments
-  How to affect values to variables
-  How to use `while` and `for` loops
-  How to use `break` and `continue` statements
-  What is a function and how do you use functions
-  What does a function that does not use any `return` statement return
-  Scope of variables
-  What are the arithmetic operators and how to use them
-  How to manipulate dictionary
-  How to import a file

## Requirements

-  Ubuntu 14.04 LTS
-  node (version 10.14.x)
-  semistandard compliant (version 14.x.x)

**Install Node 10**

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

**Install semi-standard**
[Documentation](https://github.com/standard/semistandard)

```
$ sudo npm install semistandard --global
```

## Read or watch

-  [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
-  [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
-  [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
-  [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
-  [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
-  [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
-  [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
-  [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
-  [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
-  [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)
-  [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
-  [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
-  [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## File Descriptions

This project is conceived to be carried out step by step, that is why the description of the files is presented as a statement.

### 0. First constant, first print

**[0-javascript_is_amazing.js](0-javascript_is_amazing.js)**

Write a script that prints “JavaScript is amazing”:

-  You must create a constant variable called `myVar` with the value “JavaScript is amazing”
-  You must use `console.log(...)` to print all output
-  You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
JavaScript is amazing
guillaume@ubuntu:~/0x12$
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
guillaume@ubuntu:~/0x12$
```
