import re
def is_valid_expression(expression):
    operators=r'^[\d \s\(\)\+\-\*\%]+$'
    if re.match(operators,expression):
        return True
    else:
        return False
expression1=input("Enter a mathematical expression(or 'exit' to quit):")
print(is_valid_expression(expression1))