# # occurence of each no. in a list
# def occur(l):
#     o={}
#     for num in l:
#         if num in o:
#             o[num] += 1
#         else:
#             o[num] = 1
#     return o
# l=[1, 2, 2, 3, 4, 4, 4, 5]
# for i in occur(l):
#     print(f"{i}-{occur(l)[i]}")

# #occursence of each no. in a list using lists
# def occur_list(l):
#     o=[]
#     for num in l:
#         if num not in o:
#             o.append(num)
#     for i in o:
#         print(f"{i}-{l.count(i)}")
# l=[1, 2, 2, 3, 4, 4, 4, 5]
# occur_list(l)

# #occurence of each no. in a list using sets
# def occur_set(l):
#     o=set(l)
#     for i in o:
#         print(f"{i}-{l.count(i)}")
# l=[1, 2, 2, 3, 4, 4, 4, 5]
# occur_set(l)

# #occurence of each no. in a list using collections
# from collections import Counter
# def occur_counter(l):
#     o=Counter(l)
#     for i in o:
#         print(f"{i}-{o[i]}")
# l=[1, 2, 2, 3, 4, 4, 4, 5]
# occur_counter(l)

# #find element which is repeated most no. of times in a list without functions
# l=[1, 2, 2, 3, 4, 4, 4, 5]
# o={}
# for num in l:
#     if num in o:
#         o[num] += 1
#     else:
#         o[num] = 1
# max_count=0
# max_num=None
# for i in o:
#     if o[i]>max_count:
#         max_count=o[i]
#         max_num=i
# print(f"{max_num}-{max_count}")

#single list missing element
# def missing_element(l,n):
#     l=set(l)
#     total_sum=n*(n+1)//2
#     actual_sum=sum(l)
#     return total_sum-actual_sum
# l=[1,1,2,3,4,6]
# n=6
# print(missing_element(l,n))

# #bubble sort
# def bubble_sort(l):
#     n=len(l)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
# l=[64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(l))
# print(bubble_sort([5,1,4,2,8],reverse=True))

# # [5,6,5,3,4,8,5,6]=>[1,1,2,1,1,1,3,2].. print count of each digit according to their position
# def count_position(l):
#     count_dict={}
#     result=[]
#     for num in l:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#         result.append(count_dict[num])
#     return result
# l=[5,6,5,3,4,8,5,6]
# print(count_position(l))

# l=[5,4,6,3,2,1,17,25]=>[25,5,4,6,3,2,1,17] rotate the list by 1 position towards right
# def rotate_right(l):
#     return [l[-1]] + l[:-1]
# print(rotate_right([5,4,6,3,2,1,17,25]))

# # l=[5,4,6,3,2,1,17,25]=>[4,6,3,2,1,17,25,5] rotate the list by 1 position towards left
# def rotate_left(l):
#     return l[1:] + [l[0]]
# print(rotate_left([5,4,6,3,2,1,17,25]))

# # by n positions
# l=[5,4,7,14,1,3,2,8]
# n=int(input("Enter no. of positions to rotate: "))
# b=l[n:]+l[:n]
# print(b)

# #rotate by 1 position in between given s1 and s2
# def rotate_in_between(l,s1,s2):
#     if s1<0 or s2>=len(l) or s1>=s2:
#         return "Invalid indices"
#     return l[:s1] + [l[s2]] + l[s1:s2] + l[s2+1:]
# l=[5,4,7,14,1,3,2,8]
# s1=int(input("Enter start index: "))
# s2=int(input("Enter end index: "))
# print(rotate_in_between(l,s1,s2))


#selection sort
# l=[64, 25, 12, 22, 11]
# def selectionsort(L):
#     n = len(L)
#     if n < 1:
#         return(L)
#     for i in range(n):
#         minpos = i
#         for j in range(i+1,n):
#             if L[j] < L[minpos]:
#                 minpos = j
#         (L[i],L[minpos]) = (L[minpos],L[i])
#     return(L)
# print(selectionsort(l))


#bubble sort
l=[64, 25, 12, 22, 11]
def bubble_sort(L):
    n = len(L)
    if n < 1:
        return(L)
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            (L[i],L[i+1]) = (L[i+1],L[i])
            i = 0
        else:
            i += 1
    return(L)
print(bubble_sort(l))

