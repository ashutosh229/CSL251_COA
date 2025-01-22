def binary_to_decimal(binary, bits):
    binary = binary.zfill(bits)
    value = int(binary, 2)
    if binary[0] == '1':
        value = value - (1 << bits)
    return value

def decimal_to_binary(value, bits):
    if value < 0:
        value = (1 << bits) + value
    return bin(value & ((1 << bits) - 1))[2:].zfill(bits)

def unsigned_binary_division(dividend, divisor, n_bits):
    dividend = binary_to_decimal(dividend, n_bits)
    divisor = binary_to_decimal(divisor, n_bits)

    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")

    A = 0
    M = divisor
    Q = dividend
    count = n_bits

    while count > 0:
        A = (A << 1) | ((Q >> (n_bits - 1)) & 1)
        Q = (Q << 1) & ((1 << n_bits) - 1)
        A = A - M

        if A < 0:
            Q &= ~(1)
            A += M
        else:
            Q |= 1

        count -= 1

    return Q, A

if __name__ == "__main__":
    n_bits = int(input("Enter the number of bits: "))
    dividend = input(f"Enter the {n_bits}-bit dividend in 2's complement format: ").zfill(n_bits)
    divisor = input(f"Enter the {n_bits}-bit divisor in 2's complement format: ").zfill(n_bits)

    try:
        quotient, remainder = unsigned_binary_division(dividend, divisor, n_bits)
        print("Quotient (Q):", decimal_to_binary(quotient, n_bits))
        print("Remainder (A):", decimal_to_binary(remainder, n_bits))
    except ValueError as e:
        print("Error:", e)
