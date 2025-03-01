#Create a generator comprehension that generates the first 10 numbers of the Fibonacci
#sequence.output:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
a, b = 0, 1
n=10  
for _ in range(n):
        print(a,end=" ")
        a, b = b, a + b
        # print(a,end=" ")it prints the sequence as 1 1 2 3 5 8 13 21 34 55
        
