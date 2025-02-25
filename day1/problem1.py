#Find the closest  number to zero in the given list
def closest_to_zero(lis):
    if not lis:
        return None  # Return None if the list is empty
    
    closest = lis[0]  # Assume first number is closest

    for num in lis:
        # Check if the current number is closer to zero
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    
    return closest

# Example usage
numbers = [-10, 3, 5, -2, 2, -1, 1]
print("Closest to zero:", closest_to_zero(numbers))

