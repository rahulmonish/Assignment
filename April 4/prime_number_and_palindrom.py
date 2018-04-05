for a in range(900,1001):
    k=0
    for i in range(2,a//2+1):
        if(a%i == 0):
            k=k+1
    if(k<=0):
        print("The Prime Numbers are",a)

for a in range(900,1001):
    new_number = 0
    comp_num = a
    while a > 0:
        digit = a % 10
        new_number = new_number*10 + digit
        a = a//10
    if new_number == comp_num:
        print("The Palindrom  numbers is",new_number)




