# occurence of each no. in a list
def occur(l):
    o={}
    for num in l:
        if num in o:
            o[num] += 1
        else:
            o[num] = 1
    return o
l=[1, 2, 2, 3, 4, 4, 4, 5]
for i in occur(l):
    print(f"{i}-{occur(l)[i]}")

#occursence of each no. in a list using lists
def occur_list(l):
    o=[]
    for num in l:
        if num not in o:
            o.append(num)
    for i in o:
        print(f"{i}-{l.count(i)}")
l=[1, 2, 2, 3, 4, 4, 4, 5]
occur_list(l)

#occurence of each no. in a list using sets
def occur_set(l):
    o=set(l)
    for i in o:
        print(f"{i}-{l.count(i)}")
l=[1, 2, 2, 3, 4, 4, 4, 5]
occur_set(l)