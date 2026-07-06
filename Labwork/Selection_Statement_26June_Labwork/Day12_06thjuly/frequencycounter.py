
# WAP to count the frequency of each word in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

# Count frequency of each word
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")
print(frequency)

# Find the most frequent word
max_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        max_word = word

print("\nMost Frequent Word:")
print(max_word, ":", max_count)

# Display words in alphabetical order
print("\nWords in Alphabetical Order:")
sorted_words = sorted(frequency)

for word in sorted_words:
    print(word, ":", frequency[word])

#output:
'''
    Enter a sentence: hi how are you. hey i am fine, what about you.

Word Frequency:
{'hi': 1, 'how': 1, 'are': 1, 'you.': 2, 'hey': 1, 'i': 1, 'am': 1, 'fine,': 1, 'what': 1, 'about': 1}

Most Frequent Word:
you. : 2

Words in Alphabetical Order:
about : 1
am : 1
are : 1
fine, : 1
hey : 1
hi : 1
how : 1
i : 1
what : 1
you. : 2
'''