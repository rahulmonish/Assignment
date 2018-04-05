input_sentence = 'Python is an interpreted high level programming language for general-purpose programming'

dict = {}
sentence_without_space = ''
for word in input_sentence.split(' '):
    sentence_without_space = sentence_without_space + word

print(sentence_without_space)


def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if s == rev:
        return True
    return False

palindrom_list = []
for word in input_sentence.split(' '):
    if isPalindrome(word):
        palindrom_list.append(word)
print("Palindrom List is  ",palindrom_list)

repeated_word = {}
for word in input_sentence.split(' '):
    if word in repeated_word:
        value = repeated_word.get(word)
        repeated_word[word]= value + 1
    else:
        repeated_word[word] = 1

print(repeated_word)
