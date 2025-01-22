def AddSub(a,b,op,bits):
    result_decimal = decimal_operator(a,b,op,bits)
    processed_result=handle_overflow(result_decimal,bits)
    result_binary = decimal_to_binary(processed_result,bits)
    return (result_binary,processed_result)

def decimal_to_binary(n,bits):
    if n<0:
        n = n+(1<<bits)
    binary = format(n & ((1<<bits)-1),f"0{bits}b")
    return binary

def binary_to_decimal(binary,bits):
    value = int(binary,2)
    if binary[0]=='1':
        value = value-(1<<bits)
    return value

def handle_overflow(n,bits):
    max_value = (1<<(bits-1)) - 1
    min_value = -(1<<(bits-1))
    if n>max_value:
        n = n - (1<<bits)
    if n<min_value:
        n = n + (1<<bits)
    return n

def decimal_operator(a,b,op,bits):
    a_decimal = binary_to_decimal(a,bits)
    b_decimal = binary_to_decimal(b,bits)
    if  op=="sub":
        result_decimal = a_decimal - b_decimal
    if op=="add":
        result_decimal = a_decimal + b_decimal
    return result_decimal
        
    

    
        



if __name__=="__main__":
    a = input("Enter the 1st integer in 2's complement: ")
    b = input("Enter the 2nd integer in 2's complement: ")
    result_addition_binary,result_addition_decimal = AddSub(a,b,"add",8)
    result_subtraction_binary,result_subtraction_decimal = AddSub(a,b,"sub",8)
    print(f"The result of addition of numbers in binary is: {result_addition_binary}")
    print(f"The result of addition of numbers in decimal is: {result_addition_decimal}")
    print(f"The result of subtraction of numbers in binary is: {result_subtraction_binary}")
    print(f"The result of subtraction of numbers in decimal is: {result_subtraction_decimal}")