list = [1,2,"test",4,5]

list2 = list

list[3:] = [9,10]

for i in list:
    print(i)

for j in list2:
    print(j)

list.append(list2)

print(list)



for i in range(1,10):
    if i == 3:
        break
    else:
        print(i)


tuple1 = (1,2,3)

(a,b) = (1,2)

print(a)
print(tuple1)


temparr = "vihsu"
print(temparr[0])

# u cannot change inplace value in array but can change in list

# score = {}
# test = {}
# test1 = {}
# score["test"]["pla1"] = 10
# score["test1"]["pla2"] = 20
# # score["test1"]["pla1"] = 13
#
# print(score)

obj={}

obj["key1"] = 10
obj["key2"] = 20

print(obj)

for k in sorted(obj.keys()):
    print(obj.get(k))

def power(x,n):
    res=1
    for i in range(1,n+1):
        res=res*x

    return res

print(power(n=4,x=5))





