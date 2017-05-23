num = 4;
double = 2.0000000
print(num == 4) #True
print(num == 3) #False
print(num  > 3) #True
print(num  != 3) #True
print(double == 2) #True
print(double == 2.0) #True
print(double == float(2)) #True

if num == 4 and double == 2.0 :
    print("Matches on %d AND %f" % (num, double))

if num == 5 or double == 2.0:
    print("Matches on %d OR %f" % (num, double))

name  = "Frank"
names = ["Steve", "Jane", "Frank", "Steph"]

if name in names:
    print("Found %s in %s" % (name, names))

#Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves
array_1 = ['1', '2', '3']
array_2 = ['1', '2', '3']
print(array_1 == array_2) #True
print(array_1 is array_2) #False
print(array_1 is array_1) #True

print(not True) #False
print(not True == False) #True
