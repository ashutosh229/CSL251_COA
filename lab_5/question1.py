
def binary_to_int(binary_str):
        return int(binary_str, 2)
    
def int_to_binary(num, bits):
        return bin(num)[2:].zfill(bits)

def floating_point_add_sub(n, m, s1, s2, e1, e2, flag):
    # Convert inputs to integer values
    m1 = binary_to_int('1' + s1) 
    m2 = binary_to_int('1' + s2)
    e1 = binary_to_int(e1)
    e2 = binary_to_int(e2)

    # Handle subtraction by flipping the sign of M2
    if flag == 1:
          m2 = -m2

    # Align exponents
    if e1 > e2:
        shift = e1 - e2
        m2 >>= shift 
        e2 = e1
    elif e2 > e1:
        shift = e2 - e1
        m1 >>= shift 
        e1 = e2

    # Perform addition
    m_res = m1 + m2
    e_res = e1

    # Normalize result
    if m_res == 0:
        return ["0" *n,"0"*m]

    while m_res >= (1 << (n + 1)): 
        m_res >>= 1
        e_res += 1
    while m_res < (1 << n):  
        m_res <<= 1
        e_res -= 1

    # Handle overflow/underflow
    if e_res >= (1 << m):
        return "Overflow"
    if e_res < 0:
        return "Underflow"

    # Extract final significand and exponent
    s_res = int_to_binary(m_res & ((1 << n) - 1), n) 
    e_res = int_to_binary(e_res, m)

    return [s_res ,e_res ]


if __name__=="__main__":
    
    n =int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))
    s1 = input("Enter the {n} bit string for s1: ")
    s2 = input("Enter the {n} bit string for s2: ")
    e1 = input("Enter the {m} bit string for e1: ")
    e2 = input("Enter the {m} bit string for e2: ")
    flag = int(input("Enter the value of flag(1 for addition and 0 for subtraction): "))
    result = floating_point_add_sub(n, m, s1, s2, e1, e2, flag)
    print("Result Significand :", result[0])
    print("Result Exponent :", result[1])