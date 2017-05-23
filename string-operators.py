string = "The string to 'print'"
print(len(string))
print(string.index("i"))
#ValueError: substring not found
#print(string.index("d"))

print(string.count("i"))

# [start:stop:step]
#prints string[3..7)
print(string[3:7])
print(string[-7])
print(string[-4:-1])
print(string[2:-1:3])

#reverse str
print(string[::-1])

upper = "uPPer"
lower = "LoWer"
print(upper.upper())
print(lower.lower())

#testing beginning/end
print(string.startswith("The"))
print(string.startswith("Not true"))
print(string.endswith("'print'"))
print(string.endswith("Not true"))
