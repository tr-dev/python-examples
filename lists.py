#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish.
mylist = [];
mylist.append("hello")
mylist.append(2)
mylist.append(7.0)

print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for item in mylist:
    print(item)

#IndexError: list index out of range
#print(mylist[100])
