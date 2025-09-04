#creating an empty list called my_list
my_list = []

#Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting value 15 at the second position
my_list.insert(1, 15)

# extending my_list with another list
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# Finding the value of index 30 and printing it
index_30 = my_list.index(30)
print("Index of 30:", index_30)