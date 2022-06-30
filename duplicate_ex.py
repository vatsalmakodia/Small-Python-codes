# to find duplicate in list
l = [1,2,3,4,5,6,7,8,2,4,6,8]
l1= []

for i in l:
    if l.count(i) > 1:
        if i not in l1 :
            l1.append(i)

print(l1)
