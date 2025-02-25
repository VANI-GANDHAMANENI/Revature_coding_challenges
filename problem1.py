#Find the closest  number to zero in the given list
def closest_to_zero(arr):
    if not arr:
        return None  
    
    closest = arr[0]  

    for num in arr:
        
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    
    return closest
numbers = [-10, 3, 5, -2, 2, -1, 1]
print("Closest to zero:", closest_to_zero(numbers))

