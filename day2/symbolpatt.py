# 1. Star triangle
n = 5
for i in range(1, n+1):
    print("* "*i)

# 2. Inverted star triangle
n = 5
for i in range(n,0,-1):
    print("* "*i)

# 3. Star pyramid
n = 5
for i in range(1,n+1):
    print(" "*(n-i), "* " * i)

# 4. Diamond with stars
n = 5
for i in range(1,n+1):
    print(" "*(n-i), "* " * i)
for i in range(n-1,0,-1):
    print(" "*(n-i), "* " * i)

# 5. Hollow square
n = 5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

# 6. Cross pattern
n = 5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()

# 7. Hollow triangle
n = 5
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()

# 8. Right aligned triangle
n = 5
for i in range(1,n+1):
    print(" "*(n-i), "@ "*i)

# 9. Increasing symbols
n = 5
symbols = ["*", "#", "$", "%", "&"]
for i in range(n):
    print(symbols[i]* (i+1))

# 10. Hollow diamond
n = 5
for i in range(n):
    for j in range(2*n-1):
        if j == n-i-1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n-2,-1,-1):
    for j in range(2*n-1):
        if j == n-i-1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
