#Exercise 2: List Slicing
#Given the list numbers = [11, 22, 33, 44, 55, 66, 77], use list slicing to obtain the following sublists:
#1- [22, 33, 44]
#2- [11, 33, 55, 77]
#3- [55, 44, 33, 22, 11]


numbers = [11, 22, 33, 44, 55, 66, 77]
print(numbers[1:4])
print(numbers[::2])

numbers.reverse()
print(numbers[2:])

