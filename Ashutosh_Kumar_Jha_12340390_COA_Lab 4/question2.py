from question1 import binary_to_decimal,decimal_to_binary,AddSub

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

        A_binary = decimal_to_binary(A, n_bits)
        M_binary = decimal_to_binary(M, n_bits)
        A_binary, A = AddSub(A_binary, M_binary, "sub", n_bits)

        if A < 0:
            Q &= ~(1)
            A_binary, A = AddSub(A_binary, M_binary, "add", n_bits)
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
