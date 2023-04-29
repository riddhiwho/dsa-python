num = [3,1,2,10,1]

#sol1
# sum=0
# for index, elem in enumerate(num):
#     sum+=elem
#     num[index] = sum


#sol2    
for i in range(1,len(num)):
    num[i] = num[i]+num[i-1]

print(num)