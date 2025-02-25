def rectangle_pattern(length,breadth):
    for i in range(length):
         print()
         for j in range(breadth):
            if i==0 or i==length-1 or j==0 or j==breadth-1:
                print("*",end="")
            else:
                print(" ",end="")
    
l=10
b=6
print(rectangle_pattern(l,b))

