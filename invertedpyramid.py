def inverted_pyramid(height):
    for i in range(height, 0, -1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)
height = int(input("Enter height: "))
inverted_pyramid(height)