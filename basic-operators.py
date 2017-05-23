#Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.
number = 1 + 2 * 3 / 4.0
print(number)

#mod
mod = 5 % 2
print(mod)

#powers
squared = 7 ** 2
cubed   = 3 ** 3

print(squared)
print(cubed)

#Python supports concatenating strings using the addition operator
hellworld = "hello" + " " + "word"
print(hellworld)

#Python also supports multiplying strings to form a string with a repeating sequence:
lilJon = "o" * 3 + "k" * 5
print(lilJon)

#Lists can be joined with the addition operators
evens = [2, 4, 6, 8]
odds  = [1, 3, 5, 7]
print(evens + odds)

#Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator
print([1, 2] * 3)
