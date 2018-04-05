n1 = int(input("Enter the First numbers\n"))
n2 = int(input("Enter the Second numbers\n"))
min_multiple = (n1 >= n2) and n1 or n2
while True:
    if min_multiple % n1 == 0 and min_multiple % n2 == 0:
        print("The LCM is ", min_multiple)
        break
    min_multiple = min_multiple + 1

smaller = (n1 >= n2) and n2 or n1
hcf = 0
for i in range(1, smaller+1):
    if(n1 % i == 0) and (n2 % i == 0):
        hcf = i
print("The HCF is ", hcf)

n3 = int(input("Enter the number to find its factor\n"))
factor_list = []
for i in range(1,n3+1):
    if n3%i == 0:
        factor_list.append(i)
print("Factor list of the number "+str(n3),factor_list)


