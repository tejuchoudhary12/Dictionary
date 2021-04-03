dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
        # if dic[i]<dic[j]:
            temp=dic[i]
            dic[i]=dic[j]
            dic[j]=temp
print(dic)
    