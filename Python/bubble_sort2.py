my_list = []
my_list2 = []
swapped = True
num = int(input("How many elementes do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list of elementes: "))
    my_list.append(val)
print(my_list)
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

num2 = int(input("How many elementes do you want to sort: "))
for i in range(num2):
    val = float(input("Enter a list of elementes: "))
    my_list2.append(val)
print(my_list2)
my_list2.sort()
print(my_list2)
