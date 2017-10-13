#dict: key:value; {}
#len() is to check out the length of variable.
print("********************")
print("\'key\' is not duplicated,and it does not have order.")
print("\'key\' is fixed, like integer, string, float as a key, but can't use \'list\' as a key")
dic = {
	'tom': 90,
	'jeck': 60,
	'jean': 86,
	'zhou': 77
}

#three ways is to get the value.

print("the first way")
print(dic['jean'])

print("*****************")
print("the second way")
#using ‘get method’ to get the valule, if the valule doesn's exist, return none;
print(dic.get('zhou'))

if 'ttom' in dic:
	print(dic[ttom])
else:
	print('no this person')

print("********************")
print('tom:', dic.get('tom'))
#print('tom:' + dic.get('tom'))  
#wrong, 'string + integer';
#correct, 'string + string'
print('tom:'+str(dic.get('tom')))

print("********************")
for k in dic:
	print("key: ",k)

print("********************")
for k in dic.items():
	print("key: value",k)
	
print("********************")
#if there is the same name, it will change the value, will not change key.
print("add a new iterm, may : 99")
dic['may'] = 99
print (dic)

print()

