length = int(input("Enter the length of the dictionary\n"))
dict = {}
for i in range(0, length):
    num = i
    dict[i] = num*num
print(dict)