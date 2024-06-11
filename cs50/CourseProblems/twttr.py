# vowels =['a','o','u','e','i']

# sentence = input("Input: ")

# for vowel in vowels:
#   if vowels in sentence:
#     sentence.lower().strip(vowel)
vowels = ['a', 'o', 'u', 'e', 'i']

sentence = input("Input: ")

for vowel in vowels:
    if vowel in sentence.lower():  # Check if the vowel is in the sentence (converted to lowercase)
        sentence = sentence.replace(vowel, '')  # Remove all instances of the vowel from the sentence

print(sentence)