class FloatingPointNumbers:
    def __init__(self, sign, exponent, significand):
        self.sign = sign
        self.exponent = exponent
        self.significand = significand
        
    def __str__(self):
        return f"{'-' if self.sign else ''}{self.significand}e{self.exponent}"
