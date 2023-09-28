list = [10, 5, 7, 2, 1]
print("Original list contante:", list)

list[0] = 111
print("Previous list content:", list)

list[1] = list[4] #copying value of the fifth element to the secon
print("New list content:", list)

print(list[0]) # Accessing the list's first element.
print(list) # printing the whole liest

print("List length:", len(list)) #Printing the list's length.

del list[1]
print("New list's length:", len(list)) #Printing new list length
print("New list content", list) # Printing current list content

print(list[-1]) # last argument of the list
print(list[-2]) # last but one argument of the list
print(list[-4]) # the first argument
