for item in "Python":
    print(item)
for item in ["Noob", "Saibot", "wins"]:
    print(item)
for item in range(5, 10):
    print(item)

prices = [10, 20, 30]
pricesSum = 0
for item in prices:
    pricesSum += item

print(pricesSum)

for x in range(4):
    for y in range(3):
        print("(" + str(x) + "," + str(y) + ")")

x_numbers = [5, 2, 5, 2, 2]
#My solution
for x in x_numbers:
    o = 1
    for y in range(x):

        if o == x:
            print("X")
        else:
            print("X", end="")

        o += 1

#Mosh solution

for x_count in x_numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

#List in detail
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]

#Largest number in array
largest_number = x_numbers[0]
for x in x_numbers:
    if largest_number < x:
        largest_number = x

print(largest_number)

#2d Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(9, 10)
print(numbers)
print(numbers.pop())
print(numbers)
print(50 in numbers)
print(numbers.count(7))
numbers.sort()
print(numbers)

numbers2 = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers2:
    if number not in uniques:
        uniques.append(number)
print(uniques)