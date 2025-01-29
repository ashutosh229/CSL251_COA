def binary_to_int(binary_str):
    return int(binary_str, 2)

def int_to_binary(num, bits):
    return format(num, f'0{bits}b')

def normalize_result(significand, exponent, n):
    while len(significand) > n + 1:  # Check for overflow and normalize
        significand = significand[:-1]  # Remove the least significant bit
        exponent += 1

    while significand[0] != '1' and exponent > 0:  # Normalize
        significand = significand[1:] + '0'
        exponent -= 1

    return significand, exponent

def floating_point_add_sub(n, m, S1, S2, E1, E2, flag):
    # Convert exponents to integers
    exp1 = binary_to_int(E1)
    exp2 = binary_to_int(E2)

    # Add implicit leading 1 to significands
    significand1 = '1' + S1
    significand2 = '1' + S2

    # Align exponents by shifting the smaller significand
    if exp1 > exp2:
        shift = exp1 - exp2
        significand2 = '0' * shift + significand2
        exp2 = exp1
    elif exp2 > exp1:
        shift = exp2 - exp1
        significand1 = '0' * shift + significand1
        exp1 = exp2

    # Perform addition or subtraction
    if flag == 1:  # Addition
        result_significand = bin(int(significand1, 2) + int(significand2, 2))[2:]
    else:  # Subtraction
        result_significand = bin(abs(int(significand1, 2) - int(significand2, 2)))[2:]

    # Normalize the result
    result_significand, result_exponent = normalize_result(result_significand, exp1, n)

    # Adjust the length of the significand
    result_significand = result_significand[:n]

    # Convert exponent back to binary
    result_exponent = int_to_binary(result_exponent, m)

    return result_significand, result_exponent

if __name__=="__main__":
    n = int(input("Enter the integer n: "))
    m = int(input("Enter the integer m: "))
    s1 = input(f"Enter the first {n}-bit string: ")
    s2 = input(f"Enter the second {n}-bit string: ")
    e1 = input(f"Enter the first {m}-bit string: ")
    e2 = input(f"Enter the second {m}-bit string: ")
    flag = int(input(f"Enter the flag bit(1 for addition and 0 for subtraction): "))

    result = floating_point_add_sub(n, m, s1, s2, e1, e2, flag)
    
    print("Result Significand:", result[0])
    print("Result Exponent:", result[1])
