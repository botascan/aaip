# module ex4

class ComplexNumber:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return ComplexNumber(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        return ComplexNumber(
            self.r * other.r - self.i * other.i,
            self.r * other.i + self.i * other.r
        )

    def __truediv__(self, other):
        denom = other.r ** 2 + other.i ** 2
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return ComplexNumber(
            (self.r * other.r + self.i * other.i) / denom,
            (self.i * other.r - self.r * other.i) / denom
        )
    
    def __str__(self):
        sign = "+" if self.i >= 0 else "-"
        return f"{self.r} {sign} {abs(self.i)}i"

    __repr__ = __str__
    #def __repr__(self):
    #    return f"ComplexNumber({self.r}, {self.i})"

def sum_complex(complex_numbers):
    new_r = sum(list(map(lambda c: c.r, complex_numbers)))
    new_i = sum(list(map(lambda c: c.i, complex_numbers)))
    return ComplexNumber(new_r, new_i)
