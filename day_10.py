#largest no. from a list
a=[1,7,10,34,2,8]


max = a[ 0 ]
for i in a:
	if i > max:
		max = i
print("Largest Number :",max)

#clone
old_list = [10, 22, 44, 23, 4]
new_list = list(old_list)
print("Old List : ",old_list)
print("New List : ",new_list)

#repeated items in a tuple
t = (2,34,45,6,7,2,4,5,78,34,2)
print(t)
count = t.count(2)
print(count)