class FloatingPoint:
    def __init__(self, sign, exponent, significand):
        self.sign = sign  # 0 for positive, 1 for negative
        self.exponent = exponent
        self.significand = significand

    def __str__(self):
        return f"{'-' if self.sign else ''}{self.significand}e{self.exponent}"


def align_exponents(x, y):
    while x.exponent < y.exponent:
        x.significand >>= 1
        x.exponent += 1

    while y.exponent < x.exponent:
        y.significand >>= 1
        y.exponent += 1


def add_or_subtract(x, y, operation):
    if operation == "subtract":
        y.sign = 1 - y.sign  # Change the sign of Y

    if x.sign == y.sign:
        result_significand = x.significand + y.significand
    else:
        if x.significand >= y.significand:
            result_significand = x.significand - y.significand
        else:
            result_significand = y.significand - x.significand
            x.sign = y.sign

    return x.sign, result_significand


def normalize(sign, significand, exponent):
    while significand and significand < (1 << 23):  # Normalize left
        significand <<= 1
        exponent -= 1

    while significand >= (1 << 24):  # Normalize right
        significand >>= 1
        exponent += 1

    return significand, exponent


def floating_point_add_sub(x, y, operation):
    if x.significand == 0:
        return y

    if y.significand == 0:
        return x

    align_exponents(x, y)

    sign, significand = add_or_subtract(x, y, operation)

    if significand == 0:
        return FloatingPoint(0, 0, 0)

    significand, exponent = normalize(sign, significand, x.exponent)

    return FloatingPoint(sign, exponent, significand)


# Example usage
x = FloatingPoint(0, 127, 0b10101010101010101010101)  # Example floating-point number
y = FloatingPoint(0, 126, 0b11001100110011001100110)  # Another example

# Perform addition
result_add = floating_point_add_sub(x, y, "add")
print("Addition result:", result_add)

# Perform subtraction
result_sub = floating_point_add_sub(x, y, "subtract")
print("Subtraction result:", result_sub)

