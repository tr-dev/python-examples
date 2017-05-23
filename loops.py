odds = [1, 3, 5, 7]
for odd in odds :
    print(odd)

print("-------------")

for r in range(3):
    print(r)

print("-------------")

for r in range(3, 5):
    print(r)

print("-------------")

for r in range(3, 8, 2):
    print(r)


print("-------------")

count = 0
while count < 5 :
    print(count)
    count += 1
else:
    print("Count is %s" % count)

print("-------------")
index = 0
while True :
    index += 1
    if index % 5 == 0 :
        break;
    print(index)
else:
    print("Never get here because break")
