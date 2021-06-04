my_list = ['a','b','e','w','z','q','k','a','e']

# Yield successive n-sized
# chunks from l.
def divide_group(l, n):
	
	# looping till length l
	for i in range(0, len(l), n):
		yield l[i:i + n]

# How many elements each
# list should have
n = 3

x = list(divide_group(my_list, n))
print (x)
