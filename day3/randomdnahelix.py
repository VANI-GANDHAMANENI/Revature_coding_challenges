#Write a Python program that generates a random DNA sequence of length 20 using the
# characters A , T , C , and G . Use a list comprehension to create the sequence.
import random
print([random.choice('ATCG') for _ in range(20)])

