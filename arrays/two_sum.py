num = [2,11,15,7]

target = 9

dic = {}

for i, elem in enumerate(num):
    rem = target-elem
    if rem in dic:
        print([dic[rem], i])
        break #exclude if you want to find all pairs
    else:
        dic[elem] = i