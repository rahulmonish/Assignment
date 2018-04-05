input_sentence = input("Enter the sentence\n")

sp_char = 0
upper_char = 0
lower_char = 0
number_char = 0
for letter in input_sentence:
   if letter >= 'A' and letter <= 'Z':
      upper_char = upper_char + 1
   elif letter >= 'a' and letter <= 'z':
      lower_char = lower_char + 1
   elif letter >= '0' and letter <= '9':
      digit_char= digit_char + 1
   else:
      sp_char = sp_char + 1

print("Total number of character",str(upper_char+lower_char+number_char))
print("Number of Upper character",upper_char)
print("Number of Lower character",lower_char)
print("Number of digits",digit_char)
print("Number of special character",sp_char)