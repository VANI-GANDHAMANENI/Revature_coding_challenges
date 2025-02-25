def print_right_angled_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)
height = int(input("Enter height: "))
print_right_angled_triangle(height)
