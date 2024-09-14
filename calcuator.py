value1 = float(input("Enter value1 for the calculation: "))
value2 = float(input("Enter value2 for the calculation: "))
mathematical_operation = input("Choose the mathematical operation you want(+,-,*,/):")
if mathematical_operation == '+':
    result=value1+value2
elif mathematical_operation == '-':
    result= value1 - value2   
elif mathematical_operation == '*':
    result= value1*value2
elif mathematical_operation == '/':
    if value2 !=0:
        result= value1/value2 
    else:
        result="invalid input"                
else:
    result = 'kindly choose correct operater(+,-,*,/)'    
print("ouput is: ",result)     


