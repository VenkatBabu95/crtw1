# n=int(input())
# p=n
# for i in range(1,n*2+2):
#     for j in range(1,n+2):
#         if j<=p:
#             print("* ",end=" ")
#         elif(j>p):
#             print("@ ",end=" ")
#     print()
#     if i<=n:
#         p-=1
#     else:
#         p+=1

# n=int(input())
# for i in range(n-1):
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(2*i+1):
#         print("@",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# for i in range(n-1,-1,-1):
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(2*i+1):
#         print("@",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n = 4
# for i in range(1,n+1):
#     print(" "*(n-i), "* " * i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i), "* " * i)
n=5

for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i+1:
            if (i+j)%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print(" ",end=" ")
    print()
