#!usr/bin/python/
#WAP to find out the unique value from a list?
#list = int(raw_input('Enter the value in a list:'))

list = [1,2,1,3,4,2,4,5,6,8,7,8]
list1=[]

for i in range(0,len(list)):
	if list.count(list[i])==1:
		list1.append(list[i])
print list1



