import math

a = float(input())
b = float(input())
c = float(input())

d = (b * b) - (4 * a * c)

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Two distinct and real roots exist: {r1:.2f} and {r2:.2f}")
elif d == 0:
    r1 = r2 = -b / (2 * a)
    print(f"equal and real roots exist: {r1:.2f} and {r2:.2f}")
else:
    r1 = r2 = -b / (2 * a)
    im = math.sqrt(-d) / (2 * a)
    print(f"distinct complex roots exist: {r1:.2f} + i{im:.2f} and {r2:.2f} - i{im:.2f}")
