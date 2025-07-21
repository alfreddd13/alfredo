age = {'Hans': 24, 'Prag': 23, 'Bunyod': 18}
print ("whole dictionary:", age)
print ("age of hans:", age['Hans'])
age['Prag'] = 30
print ("updated age of Prag:", age['Prag'])
del age ['Bunyod']
print ("updated dictionary:", age)