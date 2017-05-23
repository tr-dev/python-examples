#Python supports two types of numbers - integers and floating point numbers.
example_int = 1
example_float = 7.0
another_example_float = float(7)
print(example_int)
print(example_float)
print(another_example_float)
#Strings are defined either with a single quote or a double quotes.
hello = 'hello'
word =  "world"
ello = "'ello"
hello_world = '"hello world"'
print(hello)
print(word)
print(ello)
print(hello_world)

#Simple operators can be executed on numbers and strings
print(example_int + example_int)
print(example_int + example_float)
print(another_example_float + example_float)

#Assignments can be done on more than one variable "simultaneously" on the same line like this
same, line = "same", "line"
print(same)
print(line)

#Mixing operators between numbers and strings is not supported:
bad, time = 1 , "NAN"
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(bad + time)
