# 1. Increasing triangle with numbers
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 2. Repeating numbers row-wise
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()

# 3. Number pyramid
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 4. Inverted number triangle
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 5. Continuous numbers
n = 5
k = 1
for i in range(1, n+1):
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()

# 6. Diamond with numbers
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print(str(i)*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i), end="")
    print(str(i)*(2*i-1))

# 7. Floyd’s Triangle
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 8. Palindrome number pyramid
n = 5
for i in range(1, n+1):
    for j in range(i,0,-1):
        print(j, end="")
    for j in range(2,i+1):
        print(j, end="")
    print()

# 9. Number square
n = 5
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()

# 10. Number checkerboard
n = 5
for i in range(n):
    for j in range(n):
        print((i+j)%2, end=" ")
    print()

