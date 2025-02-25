def rectanglepattern(height, width):
    for _ in range(height):
        print('*' * width)
height = int(input("Enter height: "))
width = int(input("Enter width: "))
rectanglepattern(height, width)

