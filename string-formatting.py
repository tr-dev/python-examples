#The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
world = "world"
print("Hello %s" % world )

#To use two or more argument specifiers, use a tuple (parentheses)
frank = "Frank"
age   = 44;
print("Hi %s, today you are %d years old" % (frank, age))

#Any object which is not a string can be formatted using the %s operator as well.
#The string which returns from the "repr" method of that object is formatted as the string.
mylist = [1, 2, 3]
print("List: %s" % mylist )

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)
print("Float: %f" % float(10))
print("Precise Float: %.4f" % float(20))
print("Upper Hex %X, Lower Hex %x" % (15532, 15045) )
