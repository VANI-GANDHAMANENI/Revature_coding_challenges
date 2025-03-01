#  Given a sentence, use a dictionary comprehension to count the frequency of each word in
#  the sentence.
sen = "the quick brown fox jumps over the lazy dog"

count_words = {word: sen.split().count(word) for word in sen.split()}

print(count_words)

 