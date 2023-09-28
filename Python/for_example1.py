for i in range(2, 8):
    print("The value of i is currently", i)
print("//")
for i in range(2,1): #sem output
    print("The value of i is currently", i)

for i in range(2, 8, 2): #output esperado vai ser 2 4 6
    print("The value of i is currently", i)
print("//")

power = 1
for expo in range(16):
    print("3 to the power of", expo, "is", power)
    power *= 3
