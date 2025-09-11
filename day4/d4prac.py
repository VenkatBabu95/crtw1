# #sum
# n = 1234
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10

# print("Sum of digits:", total)


# #factorial of each digit
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# n=int(input())
# while(n>0):
#     digit=n%10
#     print(fact(digit))
#     n//=10




#strong number
# def factorial(x):
#     f = 1
#     for i in range(1, x + 1):
#         f *= i
#     return f

# n = 145
# temp = n
# total = 0

# while n > 0:
#     digit = n % 10
#     total += factorial(digit)
#     n //= 10

# if total == temp:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")



# #reverse
# n=789
# rev=0
# while(n>0):
#     d=n%10
#     rev=rev*10+d
#     n//=10
# print(rev)





# #palindrome
# n=1224
# temp=n
# rev=0
# while(n>0):
#     d=n%10
#     rev=rev*10+d
#     n//=10
# if rev==temp:
#     print("palindrome")
# else:
#     print("not palindrome")





# #all strong no.s in a range
# def factorial(x):
#     f = 1
#     for i in range(1, x + 1):
#         f *= i
#     return f

# for num in range(1, 501):
#     temp, total = num, 0
#     while temp > 0:
#         digit = temp % 10
#         total += factorial(digit)
#         temp //= 10
#     if total == num:
#         print(num, end=" ")




# #sum of even digit factorials
# def factorial(x):
#     f = 1
#     for i in range(1, x + 1):
#         f *= i
#     return f

# n = 3
# total = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:    # only even digits
#         total += factorial(digit)
#     n //= 10

# print(total)

## decimal to binary
# n = 13
# binary = 0
# place = 1   
# while n > 0:
#     digit = n % 2
#     binary = digit * place + binary
#     place *= 10
#     n //= 2

# print("Binary:", binary)


# #binary to decimal
# binary=11001
# decimal,power=0,0
# while binary>0:
#     digit=binary%10
#     decimal+=digit*(2**power)
#     power+=1
#     binary//=10
# print(decimal)


# #decimal to octal 
# n=25
# octal=0
# place=1
# while n>0:
#     digit=n%8
#     octal=digit*place + octal
#     place *=10
#     n//=8
# print(octal)



# #decimal to hexa
# n=255
# hexa=0
# place=1
# while n>0:
#     digit=n%16
#     hexa=digit*place+hexa
#     place*=100
#     n//=16
# print(hexa)




# # any base to decimal
# n,base=121,3
# decimal,power=0,0
# while n>0:
#     digit=n%10
#     decimal+=digit*(base**power)
#     power+=1
#     n//=10
# print(decimal)

