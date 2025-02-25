def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
result = count_words(sentence)
print("Word count:", result)
