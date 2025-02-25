def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = {}    
    for char in sentence:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1    
    return vowel_count
sentence = input("Enter a sentence: ")
result = count_vowels(sentence)
print("Vowel occurrences:", result)