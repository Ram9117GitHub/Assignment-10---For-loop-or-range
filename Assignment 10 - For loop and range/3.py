""" Write a python script to print first N natural numbers in reverse order. """
print("------------------------------------------------------------------------------------")
num = int(input("Enter a natural number:"))
for e in range(num, 0, -1):
    print(e, sep="\n")
print("---------------------------------------------------------------------------------------")
for e in range(int(input("Enter a natural number:")),0,-1):
    print(e, end=' ')
