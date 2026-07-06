# Check if a character is uppercase or lowercase
sentence = input("Enter a sentence: ")
#initialize uppercase and lowercase count as 0
uppercase = 0
lowercase = 0
for x in sentence:
    if (x >= 'A' and x <= 'Z'):
        #increment the uppercase count by 1
        uppercase += 1
    elif (x >= 'a' and x <= 'z'):
        #increment the lowercase count by 1
        lowercase += 1
print("Number of uppercase letters in the sentence:", uppercase)
print("Number of lowercase letters in the sentence:", lowercase)