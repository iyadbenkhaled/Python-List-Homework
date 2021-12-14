# Create a list that contains all the even numbers between 1 and 299.
myList = range(2,299,2)

# Iterate through the previously created list and print first the length of the list then all the squared values of the list.

print("The list contains ", len(myList), " elements.")
for i in myList:
    print(i**2) # Printing the squares of the elements
    
# In one line check if 57 is in the list using one line of python.

print("57 is in the list?", 57 in myList)
