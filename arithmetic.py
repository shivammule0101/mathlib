
def add(a, b):

  return a + b

def subtract(a, b):
 
  return a - b
def multiply(a, b):
 
  return a * b

def divide(a, b):
  if b == 0:
    return "Error: Cannot divide by zero."
  return a / b

def floor_divide(a, b):
  if b == 0:
    return "Error: Cannot divide by zero."
  return a // b 
add(5, 3)  
subtract(5, 3)  
multiply(5, 3)  
divide(5, 0)  
floor_divide(5, 3)  



