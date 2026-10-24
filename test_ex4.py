from aaip import ex4


c = ex4.ComplexNumber(2, 3)
c2 = ex4.ComplexNumber(3, 4)
print(f"ex4 Complex Numbers: {c}, {c2}")

j = complex(2, 3)
j2 = complex(3, 4)
print(f"python native Complex Numbers: {j}, {j2}")

print()

print("Try out some calculations")

print()

print("Calc with own complex numbers:")
print()

c3 = c + c2
c4 = c - c2
c5 = c * c2
c6 = c / c2

print(f"{c} + {c2} = {c3}")
print(f"{c} - {c2} = {c4}")
print(f"{c} * {c2} = {c5}")
print(f"{c} / {c2} = {c6}")

print()
print("Now python native")
j3 = j + j2
j4 = j - j2
j5 = j * j2
j6 = j / j2

print(f"{j} + {j2} = {j3}")
print(f"{j} - {j2} = {j4}")
print(f"{j} * {j2} = {j5}")
print(f"{j} / {j2} = {j6}")
