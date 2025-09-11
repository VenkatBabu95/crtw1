# n=123
# ans=0
# while(n>10):
#     d=n%100
#     ans+=d
#     n//=10
# print(ans)

# a=1
# while(n>0):
#     r=n%10
#     a*=r
#     n//=10
# print(a)


#to binary
# n,g,d=map(int,input().split())
# p=0
# c=0
# s=0
# p=0
# q=n
# rem=n%10
# if rem>=g:
#     print("Invalid")
    
# else:
#     if g==10 or d==10:
#         while(n>0):
#             r=n%d
#             q=n//d
#             c=r*(g**p)
#             s+=c
#             p+=1
#             n=q
# print(s)


# write a program to convert any given base to desired base
# constrain: conversion range will be 1-10

# def is_valid(n,g,d):
#     temp=n
#     while(temp!=0):
#         if(temp%10>=g):
#             return False
#         else:
#             temp=temp//10
#     return True

# print(is_valid(124,3,2))

# n=int(input())
# g=int(input("Enter the given Base: "))
# d=int(input("Enter the desired base"))
# if((g>=1 and g<=10) and (d>=1 and d<=10)):
#     if(is_valid(n,g)):
#         if()
#     else:
#         print("the given number with the base is not valid")
# else:
#     print("The given base or desired base should be between 1-10")


# def to_base_ten(n,g,d):
#     temp=n
#     x=0
#     desired=0
#     while(temp!=0):
#         desired=desired+temp%d*(g**x)
#         x+=1
#         temp=temp//d
#     return(desired)

# print(to_base_ten(11001,2,10))




# n=int(input())
# temp=n
# sum=0
# while(temp>=10):
#     sum=sum+temp%100
#     temp//=10
# print(sum)


# n=int(input())
# temp=n
# prod=1
# while(temp!=0):
#     prod=prod*(temp%10)
#     temp//=10
# print(prod)

# write a program to convert any given base to desired base
# constrain: conversion range will be 1-10

# def is_valid(n,g,d):
#     temp=n
#     while(temp!=0):
#         if(temp%10>=g):
#             return False
#         else:
#             temp=temp//10
#     return True
def convert(n,g,d):
    temp=n
    x=0
    desired=0
    while(temp!=0):
        desired=desired+temp%d*(g**x)
        x+=1
        temp=temp//d
    return(desired)

# n=int(input("enter a number to convert: "))
# g=int(input("Enter the given Base: "))
# d=int(input("Enter the desired base: "))
# if((g>=1 and g<=10) and (d>=1 and d<=10)):
#     if(is_valid(n,g,d)):
#         if(g==10 or d==10):
#             res=convert(n,g,d)
#             print(res)
#         else:
#             x=convert(n,g,10)
#             res=convert(x,10,d)
#             print(res)
#     else:
#         print("the given number with the base is not valid")
# else:
#     print("The given base or desired base should be between 1-10")



##new question

# n=12654
# t=n
# m=0
# while(t>1):
#     d=t%10
#     if d>=m:
#         m=d
#     t//=10
# print(m)


# newbval=convert(n,10,m)
# print(newbval)


















# def fact1(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
    
# print(fact1(5))

# while(n>1):
#     d=n%10

import math
def rev(n):
    d=int(math.log10(n))+1
    while   