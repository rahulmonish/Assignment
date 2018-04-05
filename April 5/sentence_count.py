input_sentence = input("Enter the sentence\n")
letter_count = 0
digit_count = 0
for letter in input_sentence:
    if(letter >= 'A' and letter <= 'Z')or(letter >= 'a' and letter <= 'z'):
        letter_count = letter_count + 1
    elif(letter >= '0' and letter <= '9'):
        digit_count = digit_count + 1

print("Number of letter in the sentence",letter_count)
print("Number of digit in the sentence",digit_count)

