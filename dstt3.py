#List of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

#For loops
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)

#List Comprehension
evenLC = [num for num in numbers if num % 2 == 0]
