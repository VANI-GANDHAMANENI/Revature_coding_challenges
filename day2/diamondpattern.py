def diamond(height):
    for i in range(1, height + 1, 2):
        spaces = ' ' * ((height - i) // 2)
        stars = '*' * i
        print(spaces + stars + spaces)
    for i in range(height - 2, 0, -2):
        spaces = ' ' * ((height - i) // 2)
        stars = '*' * i
        print(spaces + stars + spaces)
height = int(input("Enter an odd height: "))
if height % 2 == 0:
    print("Please enter an odd number for a symmetrical diamond.")
else:
    diamond(height)