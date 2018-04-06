paragraph_input = input("Enter the paragraph with at least 4 sentence\n")
print("The paragraph input is:\n", paragraph_input)

split_sentence = paragraph_input.split('.')

split_sentence[int(len(split_sentence)/2)] = "UST Global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial" \
                                             " Services, Telecom, Media & Technology, Insurance, Transportation & Logistics and Manufacturing" \
                                             " & Utilities."
new_sentence = ''
for sentence in split_sentence:
    new_sentence = new_sentence + " " + sentence

print("Sentence after replacement\n", new_sentence)

no_vowel = 0
upper_count = 0
lower_count = 0
sp_count = 0
for letter in paragraph_input:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u') or (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        no_vowel = no_vowel + 1
    if (letter >= 'A' and letter <= 'Z'):
        upper_count = upper_count + 1
    elif (letter >= 'a' and letter <= 'z'):
        lower_count = lower_count + 1
    elif letter != ' ':
        sp_count = sp_count + 1

print("Vowel count is ", no_vowel)
print("Upper character count is ", upper_count)
print("Lower character count is ", lower_count)
print("Special character count is", sp_count)

dict_word = {}
repeated_list = []
for word in paragraph_input.split(' '):
    if word in dict_word:
        value = dict_word.get(word)
        value = value + 1
        if value == 2:
            repeated_list.append(word)
            dict_word[word] = value
    else:
        dict_word[word] = 1

print("Repeated words are", repeated_list)

after_removing_special_char = ''
for letter in paragraph_input:
    if(letter >= 'A' and letter <= 'Z') or (letter >= 'a' and letter <= 'z') or (letter >= '0' and letter <= '9') or letter == ' ':
        after_removing_special_char = after_removing_special_char + letter

print("Sentence after removing special Character is \n", after_removing_special_char)

sentence_temp = split_sentence[len(split_sentence)-1]
split_sentence[len(split_sentence)-1] = split_sentence[0]
split_sentence[0] = sentence_temp

new_sentence_1 = ''
for sentence in split_sentence:
    new_sentence_1 = new_sentence_1 + " " + sentence

print("Sentence after swapping\n", new_sentence_1)