for i in range(1,21):
    print(i)



for i in range(1, 21):
    print(57 * i)



for i in range(1, 51):
    if (i == 15):
        continue
    if (i % 3 == 0):
        print(i)
print("End of the loop")



a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

for i in range(1, 1001):
    if (i % a == 0 and i% b == 0):
        print(i)