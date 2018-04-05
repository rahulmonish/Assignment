first = 5
second = 6
third = 7
print("Largest Number is")
if first > second and first > third:
    print(first)
elif second > first and second > third:
    print(second)
else:
    print(third)

print("Smallest Number is")
if first < second and first < third:
    print(first)
elif second < first and second < third:
    print(second)
else:
    print(third)