# n1=int(input())
# n2=int(input())
# if n1>=n2:
#     maxi=n1
# else:
#     maxi=n2
# print(f"Maximum = {maxi}")

# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>=n2 and n1>=n3:
#     maxi=n1
# elif n2>=n1 and n2>=n3:
#     maxi=n2
# elif n3>=n1 and n3>=n2:
#     maxi=n3
# print(maxi)

# n1=int(input())

# if n1>0:
#     print(f"{n1} is positive")
# elif n1<0:
#     print(f"{n1} is negative")
# else:
#     print(f"{n1} is zero")

# n1=int(input())

# if (n1%5 ==0) and (n1%11 ==0):
#     print("divisible by 5 and 11")
# else:
#     print("not divisible by 5 and 11")

# n1=int(input())
# if n1%2==0:
#     print("even")
# else:
#     print("odd")
# year=int(input())
# if (year % 400 == 0) and (year % 100 == 0): 
#     print("leap year")
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("leap year")
# else:
#     print("not a leap year")

# a=input()
# if (65<=ord(a)<=90) or (97<=ord(a)<=122):
#     print("alphabet")
# else:
#     print("not an alphabet")

# a=input()
# if a in 'aeiouAEIOU':
#     print(f"{a} is vowel")
# else:
#     print(f"{a} is a consonant")
# ch=input()
# if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
#     print(f"{ch} is letter")
# elif(ch >= '0' and ch <= '9'):
#     print(f"{ch} is digit")
# else:
#     print(f"{ch} is a special character")

# a=input()
# if 'A'<=a<='Z':
#     print(f"{a} is uppercase")
# elif 'a'<=a<='z':
#     print(f"{a} is lowercase")

# w=int(input())
# if w==1:
#     print("Monday")
# elif w==2:
#     print("Tuesday")
# elif w==3:
#     print("Wednesday")
# elif w==4:
#     print("Thursday")
# elif w==5:
#     print("Friday")
# elif w==6:
#     print("Saturday")
# else:
#     print("Sunday")

# m=int(input())
# if m == 1:
#     print("31 days")
# elif m == 2:
#     print("28 or 29 days")
# elif m == 3:
#     print("31 days")
# elif m == 4:
#     print("30 days")
# elif m == 5:
#     print("31 days")
# elif m == 6:
#     print("30 days")
# elif m == 7:
#     print("31 days")
# elif m == 8:
#     print("31 days")
# elif m == 9:
#     print("30 days")
# elif m == 10:
#     print("31 days")
# elif m == 11:
#     print("30 days")
# elif m == 12:
#     print("31 days")


# note500 = note100 = note50 = note20 = note10 = note5 = note2 = note1 = 0
# amount = int(input("Enter amount: "))
# if amount >= 500:
#     note500 = amount // 500
#     amount -= note500 * 500
# if amount >= 100:
#     note100 = amount // 100
#     amount -= note100 * 100
# if amount >= 50:
#     note50 = amount // 50
#     amount -= note50 * 50
# if amount >= 20:
#     note20 = amount // 20
#     amount -= note20 * 20
# if amount >= 10:
#     note10 = amount // 10
#     amount -= note10 * 10
# if amount >= 5:
#     note5 = amount // 5
#     amount -= note5 * 5
# if amount >= 2:
#     note2 = amount // 2
#     amount -= note2 * 2
# if amount >= 1:
#     note1 = amount

# print("Total number of notes =")
# print(f"500 = {note500}")
# print(f"100 = {note100}")
# print(f"50 = {note50}")
# print(f"20 = {note20}")
# print(f"10 = {note10}")
# print(f"5 = {note5}")
# print(f"2 = {note2}")
# print(f"1 = {note1}")

# angle1, angle2, angle3 = map(int, input().split())
# sum_of_angles = angle1 + angle2 + angle3
# if sum_of_angles == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
#     print("Triangle is valid.")
# else:
#     print("Triangle is not valid.")

# s1, s2, s3 = map(int, input().split())

# if (s1 + s2) > s3:
#     if (s2 + s3) > s1:
#         if (s1 + s3) > s2:
#             print("Triangle is valid.")
#         else:
#             print("Triangle is not valid.")
#     else:
#         print("Triangle is not valid.")
# else:
#     print("Triangle is not valid.")

# a, b, c = map(int, input().split())

# if a == b and b == c:
#     print("Equilateral triangle.")
# elif a == b or a == c or b == c:
#     print("Isosceles triangle.")
# else:
#     print("Scalene triangle.")

# import math

# a, b, c = map(float, input().split())

# d = (b * b) - (4 * a * c)

# if d > 0:
#     r1 = (-b + math.sqrt(d)) / (2 * a)
#     r2 = (-b - math.sqrt(d)) / (2 * a)
#     print(f"distinct and real roots: {r1:.2f} and {r2:.2f}")
# elif d == 0:
#     r1 = r2 = -b / (2 * a)
#     print(f"equal and real roots: {r1:.2f} and {r2:.2f}")
# else:
#     r1 = r2 = -b / (2 * a)
#     imaginary = math.sqrt(-d) / (2 * a)
#     print(f"Two distinct complex roots exist: {r1:.2f} + i{imaginary:.2f} and {r2:.2f} - i{imaginary:.2f}")


# cp = int(input(""))
# sp = int(input(""))

# if sp > cp:
#     amt = sp - cp
#     print(f"Profit = {amt}")
# elif cp > sp:
#     amt = cp - sp
#     print(f"Loss = {amt}")
# else:
#     print("No Profit No Loss.")

# m1=int(input())
# m2=int(input())
# m3=int(input())
# m4=int(input())
# m5=int(input())
# s=m1+m2+m3+m4+m5
# t=500
# p=(s/t)*100

# if p>=90:
#     print("Grade A")
# elif p>=80:
#     print("Grade B")
# elif p>=70:
#     print("Grade C")
# elif p>=60:
#     print("Grade D")
# elif p>=40:
#     print("Grade E")
# else:
#     print("Grade F")

# b = float(input())

# if b <= 10000:
#     da = b * 0.8
#     hra = b * 0.2
# elif b <= 20000:
#     da = b * 0.9
#     hra = b * 0.25
# else:
#     da = b * 0.95
#     hra = b * 0.3

# gross = b + hra + da

# print(f"GROSS SALARY OF EMPLOYEE = {gross:.2f}")


# u = int(input("Enter total units consumed: "))

# if u <= 50:
#     a = u * 0.50
# elif u <= 150:
#     a = 25 + ((u - 50) * 0.75)
# elif u <= 250:
#     a = 100 + ((u - 150) * 1.20)
# else:
#     a = 220 + ((u - 250) * 1.50)

# s = a * 0.20
# t = a + s

# print(f"Electricity Bill = Rs. {t:.2f}")
