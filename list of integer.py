user_input = input("Enter a list of integers separated by spaces: ")
numbers_str = user_input.split()
numbers = [int(num) for num in numbers_str]
result = []
for num in numbers:
    if num > 100:
        result.append("over")
    else:
        result.append(num)

print(result)