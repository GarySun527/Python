#we use '\' to declear special notations.
#if there are a lot of special notations needed to translate: r'....'

print ('we will declear a \'list\'')
list = ['ID','Tom','28','male','worker']
#if it's python 3, it's 'print (L)'; if it's python 2, 'print L';
print (list)

print('************************\n')
print('pop(0) is to point a specific element got and deleted.')
print (list.pop(0))
print (list)

print('************************\n')
print('pop means to get the last element and delete it from the list.')
print (list.pop())
print (list)

print('************************\n')
print('list[-1] means to get the last element.')
print (list[-1])
print(list)

print('************************\n')
print('list.append() is to add an element in the last.')
print (list.append('address'))
print(list,'\n')
print('list.insert() is to point a specific location.')
list.insert(0,'dummy')
print(r"list.insert(0,'dummy')")
print(list)

print('************************\n')
print('lis[0] = \'mm\' is to replace an element.')
print(list)
list[0] = 'Element'
print(r"list[0] = 'Element'")
print(list)


