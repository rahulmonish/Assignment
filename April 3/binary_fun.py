number_of_input = int(input("Enter lenght of the List\n"))
input_numbers = []
print("Enter the numbers")
for i in range(0, number_of_input):
    input_numbers.append(int(input()))

input_numbers.sort() #sort the number list
print(input_numbers)
searched_element = int(input("Enter the numbers to be searched in the list\n"))
lower_bound = 0
flag = 0
upper_bound = len(input_numbers) - 1
while lower_bound < upper_bound:
    mid = int((lower_bound+upper_bound)/2)
    if input_numbers[mid] == searched_element:
        flag = 1
        break
    elif input_numbers[mid] > searched_element:
        upper_bound = mid - 1
    elif input_numbers[mid] < searched_element:
        lower_bound = mid + 1

if flag == 1:
    print("Number is found at index",mid)
else:
    print("Number is not found in the list")
