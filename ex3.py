def returnSum(myDict): 
    
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
    
    return sum

dict = {'data1':100,
        'data2': -54,
        'data3': 247} 
print("Sum :", returnSum(dict))