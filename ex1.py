from collections import Counter
# counter collects data in unorder collection
#counts another elements form counter

dic1 = Counter({1:10, 2:20})
dic2 = Counter({3:30,2:40})
dic3 = Counter({5:50,6:60})

final_dictionary= dic1 + dic2 + dic3 
  
print ("final dictionary", + (final_dictionary))