sentence = "this is a common interview question"
char_frequency ={}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print (char_frequency)
sorted_freq = sorted(char_frequency.items(), key= lambda x: x[1], reverse= True)
print(sorted_freq)
print("Most repeated char: ", sorted_freq[0])