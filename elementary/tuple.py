#tuple don't have append(),pop(),insert();
#tuple can't be changed, the size is fixed, if we build a tuple.
#we can use the index to get the elements, like list;

tp = ('adam', 'lisa', 'tom', 'jeck')
print(tp)

print("******************")
print(r"tuple[0] is to get the element and don't delete it.")
print(tp[0])
print(tp)

print("******************")
#it must name 'tuple'; print the range from 0 to 9;
t = tuple(range(0,10))
print(t)

print("******************")
#it's tuple below.
tpl = ()
print(tpl)
#it's not tuple below. it's a integer 1. () is precedence.
tpl = (1)
print(tpl)
#if there is only 1 element in tuple, we have to add a notation ',' like (1,)
tpl = (1,)
print(tpl)

print("******************")
print("how to build a flexiable tuple?, we can add a list in tuple.")
fle_list = [5, 6, 7]
fle_tuple = (1,3, fle_list)
print(fle_tuple)
fle_tuple = (1,3, [8,10])
print(fle_tuple)

print("******************")
print("we can add, delete or change the elelemt in list.")
clist = fle_tuple[2]
clist[0] = 'x'
clist[1] = 'y'
print(fle_tuple)