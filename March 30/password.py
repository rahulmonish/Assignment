import re
def length(s):
    if len(s)>=8 and len(s)<=14:
        return True

def capital_letter(s):
    count = 0
    for letter in s:
        if letter>='A' and letter<='Z':
           count = count + 1
    if count >= 1:
        return True
    else:
        return False

def check_number(s):
    count = 0
    for letter in s:
        if letter>='0' and letter<='9':
           count = count + 1
    if count >= 1:
        return True
    else:
        return False

def check_special(s):
    if len(re.findall('[^A-Za-z0-9]', s))>0:
        return True
    else:
        return False


if __name__ == "__main__":
    password = input("Enter the password\n")
    if check_special(password) and check_number(password) and length(password) and capital_letter(password):
        print("Valid")
    else:
        print("Invalid")