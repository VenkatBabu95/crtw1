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
# n=5

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=n-i+1:
#             if (i+j)%2==0:
#                 print("1",end=" ")
#             else:
#                 print("0",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# s=1
# e=n+1
# for i in range(1,n+1):
#     if i%2==0:
#         for j in range(1,n+2):
            
#                 print(i,end=" ")
#         print()
#         s+=1
#     else:
#         for j in range(1,n+1):
            
#                 print(i,end=" ")
#         s+=1
#         print()




# n = int(input())
# while(n>0):
#   r = n % 10
#   print(r,end = ",")
#   n = n // 10
# while(n>10):
#   r = n % 100
#   print(r,end = " ")
#   n = n // 100
# while(n>0):
#   r = n % 100
#   print(r,end = " ")
#   n = n // 100


# while(n>10):
#   r = n % 100
#   print(r,end = " ")
#   n = n // 100


# while(n>10):
#   r = n % 1000
#   print(r,end = " ")
#   n = n // 10


#no. of evens
#n=int(input())
# c=0
# while(n>1):
#     d=n%10
#     if d%2==0:
#         c+=1
#     n=n//10
# print(c)

#reverse
# n1=0
# while(n>0):
#     r=n%10
#     n1=n1*10+r
#     n=n//10
# print(n1)

#palindrome
# n1=0
# n2=n
# while(n>0):
#     r=n%10
#     n1=n1*10+r
#     n=n//10
# if n1==n2:
#     print("palindrome")
# else:
#     print("not palindrome")

#count even count odd
# n=int(input())
# ce=0
# co=0
# while(n>1):
#     d=n%10
#     if d%2==0:
#         ce+=1
#     elif d%2!=0:
#         co+=1
#     n=n//10
# print(ce)
# print(co)

# postional even odd

# n = int(input())
# temp = n
# count = 0
# while temp > 0:
#     count += 1
#     temp = temp // 10
# ce = 0  
# co = 0  
# for pos in range(1, count + 1):
#     divisor = 10 ** (count - pos)
#     digit = (n // divisor) % 10

#     if pos % 2 == 0 and digit % 2 == 0:
#         ce += 1
#     elif pos % 2 != 0 and digit % 2 != 0:
#         co += 1

# print(ce)
# print(co)



