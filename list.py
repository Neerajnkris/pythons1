from itertools import count

list1 = [10, 20, 30, 40, 50]
list2 = [10, 15, 30, 45, 50]
l1c = len(list1)
l2c = len(list2)
if l1c == l2c:
    print("2 list are same numbers of element")

s1c = 0
for num in list1:
    s1c += num
s2c = 0
for num in list2:
    s2c += num
if s1c == s2c:
    print("2 list of sum are same")
else:
    print("2 list of sum are not same ")

common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print("Values that occur in both lists:", common_elements)