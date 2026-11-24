sentence = "python is easy and python is fun"

print("Sentence:", sentence)

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print("Word Frequency Dictionary:", word_count)

for word, count in word_count.items():
    print(word, ":", count)
