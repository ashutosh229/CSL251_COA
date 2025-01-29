'''
Implement floating-point addition/subtraction following the attached flow-chart.
 
Your program takes the following as inputs: 
integers n and m; 
two n-bit strings S1 and S2; 
two m-bit strings E1 and E2; 
a flag bit denoting addition or subtraction. 

The floating-point numbers under consideration are: 
A=1.S1x2^E1 
B=1.S2x2^E2

The output of the program is A+B or A-B based on the flag-bit.

'''

import FloatingPointNumbers 

def script(a: FloatingPointNumbers,b: FloatingPointNumbers,flag):
    if a.significand == 0:
        return b 
    if b.significand == 0:
        return a
    
    




if __name__=="__main__":
    n = int(input("Enter the integer n: "))
    m = int(input("Enter the integer m: "))
    s1 = input(f"Enter the first {n}-bit string: ")
    s2 = input(f"Enter the second {n}-bit string: ")
    e1 = input(f"Enter the first {m}-bit string: ")
    e2 = input(f"Enter the second {m}-bit string: ")
    flag = input(f"Enter the flag bit(1 for addition and 0 for subtraction): ")
    
    A = FloatingPointNumbers(1,e1,s1)
    B = FloatingPointNumbers(1,e2,s2)
    
    result = script(A,B,flag)
    
    if flag==1:
        operation = "addition"
    else:
        operation="subtraction"
    print(f"The result after {operation} of the given numbers is: {result}")
       
