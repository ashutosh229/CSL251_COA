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

def align_exponents(a,b):
    if a.significand < b.significand:
        a.significand >>= 1
        a.exponent = a.exponent + 1
    if a.significand > b.significand:
        b.significand >>= 1
        b.exponent = b.exponent + 1
        
def add_subtract(a,b,flag):
    if flag==0:
        b.sign = 1-b.sign
    if a.sign == b.sign:
        result_significand = a.significand + b.significand
    else:
        if (a.significand>=b.significand):
            result_significand = a.significand - b.significand
        else:
            result_significand = b.significand - a.significand
            a.sign = b.sign
    return a.sign, result_significand 

def normalize(sign,significand,exponent):
    while significand and significand<(1<<23):
        significand <<= 1
        exponent = exponent -1 
    while (significand>=(1<<24)):
        significand>>=1
        exponent = exponent + 1
        
    return significand, exponent  
            

def script(a: FloatingPointNumbers,b: FloatingPointNumbers,flag):
    if a.significand == 0:
        return b 
    if b.significand == 0:
        return a
    
    align_exponents(a,b)
    a_sign, result_significand = add_subtract(a,b,flag)
    
    if result_significand==0:
        return FloatingPointNumbers(0,0,0)
    significand, exponent = normalize(a_sign,result_significand,a.exponent)
    return FloatingPointNumbers(flag, exponent, significand)

    
    
    




if __name__=="__main__":
    n = int(input("Enter the integer n: "))
    m = int(input("Enter the integer m: "))
    s1 = input(f"Enter the first {n}-bit string: ")
    s2 = input(f"Enter the second {n}-bit string: ")
    e1 = input(f"Enter the first {m}-bit string: ")
    e2 = input(f"Enter the second {m}-bit string: ")
    flag = int(input(f"Enter the flag bit(1 for addition and 0 for subtraction): "))
    
    A = FloatingPointNumbers(1,e1,s1)
    B = FloatingPointNumbers(1,e2,s2)
    
    result = script(A,B,flag)
    
    if flag==1:
        operation = "addition"
    else:
        operation="subtraction"
    print(f"The result after {operation} of the given numbers is: {result}")
       
