def safeDivide(dividend, divisor):
    if divisor == 0:
       return None
    else:
       return dividend / divisor
       

x = safeDivide(3, 0)
y = safeDivide(3, 4)
z = safeDivide(2, 3)