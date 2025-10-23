user_input = input("Enter numbers separated by commas: ")
li = [int(x) for x in user_input.split(",")]

total = 0
for i in li:
    total = total + i

print("The sum of the list is", total)

