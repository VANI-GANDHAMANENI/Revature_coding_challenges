#Write a Python program that uses a set comprehension to extract all unique alphabetic
# characters from a given string, ignoring case.
from collections import OrderedDict
def characters(str):
   return OrderedDict.fromkeys([char.lower() for char in str if char.isalpha()])
#to print the text in order of the given input
#gives the output in random order
   # return {char.lower() for char in str if char.isalpha()} 
text="hello world"
order=characters(text)
print(f"{{{', '.join(order.keys())}}}")