# Check if a character is a special character in a given sentence
sentence = input("Enter a sentence: ")
#initialize special character count as 0
special_chars = 0
for x in sentence:
    if not (x.isalnum()):
        #increment the special character count by 1
        special_chars += 1
print("Number of special characters in the sentence:", special_chars)