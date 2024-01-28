#Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list
# such that the new list should contain odd numbers from the first list and even numbers from the second list.

# create lists
first_list = [10, 20, 25, 30, 35]
second_list = [40, 45, 60, 75, 90]
new_list = []

for i in first_list:

    check = i % 2

    if check == 0:
        continue
    else:
        new_list.append(i)

for i in second_list:

    check = i % 2

    if check == 0:
        new_list.append(i)
    else:
        continue



