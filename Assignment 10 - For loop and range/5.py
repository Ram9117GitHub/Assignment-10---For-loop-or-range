""" Write a python script to print first N odd natural numbers in reverse order """
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural number:"))
for e in range(num, 0, -2):
    print(e)
print("-----------------------------------------------------------------------------------------------------------------")
for e in range(int(input("Enter a Natural number:")), 0, -2):
    print(e)
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural numbers :"))
for e in range(1, num):
    if num % 2 == 0:
        break
    else:
        print(num)
        num -= 2
print("----------------------------------------------------------------------------------------------------------------")