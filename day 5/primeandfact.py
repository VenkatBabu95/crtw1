# #factorial meth 1
# n=12
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=", ")

# #factorial meth 2
# n=12
# for i in range(2,int(n**0.5+1)):
#     if n%i==0:
#         print(i,end=", ")
#         print(n//i,end=", ")
# print(1,n,sep=", ")


#count factors
# n=49
# count=2
# for i in range(2,int(n**0.5+1)):
#     if n%i==0:
#         if n//i==i:
#             print(i,end=", ")
#             count+=1
#         else:
#             print(i,end=", ")
#             print(n//i,end=", ")
#             count+=2
# print(1,n,sep=", ")
# print("Total factors:",count)


#perfect square
# n=12
# count=2
# for i in range(2,int(n**0.5+1)):
#     if n%i==0:
#         if n//i==i:
#             print(i,end=", ")
#             count+=1
#         else:
#             print(i,end=", ")
#             print(n//i,end=", ")
#             count+=2
# print(1,n,sep=", ")
# print("Total factors:",count)
# if count%2==0:
#     print("not a perfect square")
# else:
#     print("perfect square")


# perfect and not perfect square count in a list 
# l=[13,15,18,25,16]
# cp=0
# cnp=0
# for n in l:
#     #count factors
#     count=2
#     for i in range(2,int(n**0.5+1)):
#         if n%i==0:
#             if n//i==i:
#                 print(i,end=", ")
#                 count+=1
#             else:
#                 print(i,end=", ")
#                 print(n//i,end=", ")
#                 count+=2
#     if count%2==0:
#         cnp+=1
#     else:
#         cp+=1
# print("\nperfect square count:",cp)
# print("not a perfect square count:",cnp)


# #prime number

# l=[13,15,18,25,16]
# p=0
# np=0
# for n in l:
#     #count factors
#     count=2
#     for i in range(2,int(n**0.5+1)):
#         if n%i==0:
#             if n//i==i:
#                 print(i,end=", ")
#                 count+=1
#             else:
#                 print(i,end=", ")
#                 print(n//i,end=", ")
#                 count+=2
#     if count==2:
#         p+=1
#     else:
#         np+=1
# print("\nprime:",p)
# print("not prime:",np)


# #primes in given range
# l,r=10,20
# for n in range(l,r+1):
#     count=2
#     for i in range(2,int(n**0.5+1)):

#         if n%i==0:
#             if n//i==i:
#                 count+=1
#             else:
#                 count+=2
#     if count==2:
#         print(n,end=", ")



# # primes and not primes in given range using flag
# l, r = 10, 20
# prime_count = 0
# not_prime_count = 0

# for n in range(l, r + 1):
#     is_prime = True
#     if n < 2:
#         is_prime = False
#     else:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         prime_count += 1
#         print(f"{n} is prime")
#     else:
#         not_prime_count += 1
#         print(f"{n} is not prime")

# print(f"\nPrime count: {prime_count}")
# print(f"Not prime count: {not_prime_count}")



# ...existing code...

# #lowest prime and highest non prime in a range
# l, r = 10, 20
# lowest_prime = None
# highest_non_prime = None

# for n in range(l, r + 1):
#     is_prime = True
#     if n < 2:
#         is_prime = False
#     else:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         lowest_prime = n if lowest_prime is None else min(lowest_prime, n)
#         print(f"{n} is prime")
#     else:
#         highest_non_prime = n if highest_non_prime is None else max(highest_non_prime, n)
#         print(f"{n} is not prime")

# print(f"\nLowest prime: {lowest_prime}")
# print(f"Highest non-prime: {highest_non_prime}")


# #lowest prime and highest non prime factorials in a number
# n = 1234567890
# lowest_prime = None
# highest_non_prime = None

# temp = n
# while temp > 0:
#     digit = temp % 10
#     temp //= 10

#     is_prime = True
#     if digit < 2:
#         is_prime = False
#     else:
#         for i in range(2, int(digit ** 0.5) + 1):
#             if digit % i == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         lowest_prime = digit if lowest_prime is None else min(lowest_prime, digit)
#         print(f"{digit} is prime")
#     else:
#         highest_non_prime = digit if highest_non_prime is None else max(highest_non_prime, digit)
#         print(f"{digit} is not prime")

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# print(fact(lowest_prime))
# print(fact(highest_non_prime))

# #fibonacci
# n1=0
# n2=1
# r=10
# fib=0
# for i in range(10):
#     print(fib,end=", ")
#     fib=n1+n2
#     n1=n2
#     n2=fib


# ## fibo 2 
# n=int(input())
# n1=2
# n2=3
# n3=0
# sum1=0
# sum2=0
# print(n1,n2,n3)
# for i in range(4,n+1):
#     sum1=n1+n2+n3
#     print(sum1)
#     n1=n2
#     n2=n3
#     n3=sum1
# ## fibo 3
# n=int(input())
# n1=2
# n2=3
# n3=0
# sum1=0
# sum2=0
# print(n1,n2,n3)
# for i in range(4,n+1):
#     sum1=n1+n2+n3
#     sum2+=sum1
#     print(sum1)
#     n1=n2
#     n2=n3
#     n3=sum1
# print(sum2)



a,b=map(int,input().split())
def gcd(a,b):
    ans=0
    while True:
        rem=a%b
        if(rem==0):
            ans=b
            break
        a=b
        b=rem
    return ans
print((a*b)//gcd(a,b))


