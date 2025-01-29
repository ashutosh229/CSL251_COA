def binary_to_int(binary_str):
    """
    Convert a binary string to an integer.
    """
    return int(binary_str, 2)

def int_to_binary(num, bits):
    """
    Convert an integer to a binary string of fixed length.
    """
    return format(num, f'0{bits}b')

def normalize_result(significand, exponent, n):
    """
    Normalize the result by shifting the significand and adjusting the exponent.
    """
    while len(significand) > n + 1:  # Check for overflow and normalize
        significand = significand[:-1]  # Remove the least significant bit
        exponent += 1

    while significand[0] != '1' and exponent > 0:  # Normalize
        significand = significand[1:] + '0'
        exponent -= 1

    return significand, exponent

def floating_point_add_sub(n, m, S1, S2, E1, E2, flag):
    """
    Perform floating-point addition or subtraction based on the provided flag.

    Inputs:
        n: Number of bits for significand.
        m: Number of bits for exponent.
        S1: Binary string representing the significand of A.
        S2: Binary string representing the significand of B.
        E1: Binary string representing the exponent of A.
        E2: Binary string representing the exponent of B.
        flag: 1 for addition, 0 for subtraction.

    Output:
        Result of A+B or A-B as a tuple of binary strings (significand, exponent).
    """
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

# Example Usage
n = 4  # Significand bits
m = 3  # Exponent bits
S1 = '1010'  # Significand of A
S2 = '0110'  # Significand of B
E1 = '010'  # Exponent of A
E2 = '001'  # Exponent of B
flag = 1  # 1 for addition, 0 for subtraction

result = floating_point_add_sub(n, m, S1, S2, E1, E2, flag)
print("Result Significand:", result[0])
print("Result Exponent:", result[1])
