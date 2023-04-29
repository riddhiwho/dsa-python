num = [0,1,0,3,12]

#sol 1
# for i in range(len(num)):
#     if num[i] == 0:
#         num.append(num.pop(i))

#sol2
# count = 0
# for i in range(len(num)):
#     if num[i]!=0:
#         num[count] = num[i]
#         count+=1

# while(count<len(num)):
#     num[count] = 0
#     count+=1
 

#sol3
j=0
for i in range(len(num)):
    if num[i]!=0:
        num[j], num[i] = num[i], num[j]
        j+=1   
    
print(num)