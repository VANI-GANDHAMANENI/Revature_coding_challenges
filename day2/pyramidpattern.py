def pyramidpattern(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)

# Example usage
height = int(input("Enter height: "))
pyramidpattern(height)
