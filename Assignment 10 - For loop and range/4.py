""" Write a python script to print first N odd natural numbers """
num = int(input("Enter a  Natural number:"))
print("---------------------------------------------------------------------------------------------------------------")
for e in range(1,num+1,2):
    print(e)
print("---------------------------------------------------------------------------------------------------------------")
for e in range(1,int(input("Enter a Natural number :"))+1, 2):
    print(e)
print("----------------------------------------------------------------------------------------------------------------")