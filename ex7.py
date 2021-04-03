dic1= [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]   
a=list(set(val for dic in dic1 for val in dic.values()))
print("Final List of unique values"+ str (a))



