def print_hollow_rectangle(height, width):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*') 
height = int(input("Enter height: "))
width = int(input("Enter width: "))
print_hollow_rectangle(height, width)