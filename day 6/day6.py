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

#find element which is repeated most no. of times in a list without functions
l=[1, 2, 2, 3, 4, 4, 4, 5]
o={}
for num in l:
    if num in o:
        o[num] += 1
    else:
        o[num] = 1
max_count=0
max_num=None
for i in o:
    if o[i]>max_count:
        max_count=o[i]
        max_num=i
print(f"{max_num}-{max_count}")