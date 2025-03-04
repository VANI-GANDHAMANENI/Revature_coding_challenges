def calculate(expression):
    try:
        eval(expression)
        return True
    except (SyntaxError,NameError, TypeError, ZeroDivisionError):
        return False
    
stri=input("Enter an expression:")
print(calculate(stri))
number1 = float(input('Enter first number: ')) 
op = input('Enter operator (+,-,*,/,^): ') 
number2 = float(input('Enter second number: ')) 
print(number1,op,number2)
def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result =  n1*n2
    elif op == '/':
        result = n1/n2
    elif op=='^':
        result =  n1**n2
# return result