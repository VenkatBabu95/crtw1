n = int(input())

size = 2 * n - 1  # total rows and columns

for i in range(size):
    for j in range(size):
        top = i                # distance from top
        left = j               # distance from left
        bottom = size - 1 - i  # distance from bottom
        right = size - 1 - j   # distance from right

        min_dist = min(top, left, bottom, right)
        print(n - min_dist, end=" ")
    print()
