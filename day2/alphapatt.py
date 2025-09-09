# 1. Increasing triangle with alphabets
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()

# 2. Repeating alphabets row-wise
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65+i), end=" ")
    print()

# 3. Alphabet pyramid
n = 5
for i in range(n):
    print(" "*(n-i-1), end="")
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()

# 4. Inverted alphabet triangle
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()

# 5. Continuous alphabet sequence
n = 5
k = 65
for i in range(n):
    for j in range(i+1):
        print(chr(k), end=" ")
        k += 1
    print()

# 6. Diamond with alphabets
n = 5
for i in range(n):
    print(" "*(n-i-1), end="")
    print(chr(65+i)*(2*i+1))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1), end="")
    print(chr(65+i)*(2*i+1))

# 7. Right-angled triangle with reversed alphabets
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-j-1), end=" ")
    print()

# 8. Palindrome alphabet pyramid
n = 5
for i in range(n):
    for j in range(i, -1, -1):
        print(chr(65+j), end="")
    for j in range(1, i+1):
        print(chr(65+j), end="")
    print()

# 9. Alphabet square
n = 5
for i in range(n):
    for j in range(n):
        print(chr(65+j), end=" ")
    print()

# 10. Alphabet checkerboard
n = 5
for i in range(n):
    for j in range(n):
        print(chr(65+(i+j)%2), end=" ")
    print()




