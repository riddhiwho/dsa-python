num = [2,2,1,1,1,2,2]
# num = [3,2,3]

# dic={}

# for i in num:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
        
# for key, val in dic.items():
#     if val>len(num)/2:
#         print(key)
#         break


majority = num[0]
count=1

for i in range(1,len(num)):
    if num[i]==majority:
        count+=1
    else:
        count-=1
    if count==0:
        majority = num[i]
        count=1

print(majority)
print(count)
    