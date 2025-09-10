# n=5 
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n=5 
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# for i in range(n+1):
#     print(" "*(n-i),"*"*i)

# for i in range(n+1):
#     print("*"*(n-i)," "*i)

# n=5
# s=n
# e=n
# for i in range(n+1):
#     for j in range(2*n+1):
#         if j>=s and j<=e:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     s-=1
#     e+=1



# n=5
# s=n
# e=2*n-1
# for i in range(1,n+1):
#     for j in range(1,2*n+1):
#         if j>=s and j<=e:
#             print("*",end=" ")
#         elif(j<s or j>e):
#             print(" ",end=" ")
#     print()
#     s+=1
#     e-=1

# rows=5
# for i in range(rows, 0, -1):  
#         for j in range(rows - i):
#             print(" ", end="")
#         for k in range(2 * i - 1):
#             print("*", end="")
#         print()

# n=5
# s=n
# e=n
# for i in range(n+1):
#     for j in range(2*n+1):
#         if j>=s and j<=e:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     s-=1
#     e+=1
# s=1
# e=2*n-1
# for i in range(n+1):
#     for j in range(2*n+1):
#         if j>=s and j<=e:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     s+=1
#     e-=1


# n=5
# s=n
# e=n
# for i in range(n+1):
#     for j in range(2*n+1):
#         if j>=s and j<=e:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     s-=1
#     e+=1
# s=0
# e=2*n
# for i in range(n+1):
#     for j in range(2*n+1):
#         if j>=s and j<=e:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     s+=1
#     e-=1

n=5 
for i in range(n):
    for  j in range(n):
        if i>=j:
            print("*",end=" ")
    print()
for i in range(1,n):
    for  j in range(n):
        if i<=j:
            print("*",end=" ")
    print()

