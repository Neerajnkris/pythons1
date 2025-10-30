import math

for n in range(int(math.sqrt(1000)), int(math.sqrt(9999)) + 1):
    sq = n * n
    if all(int(d) % 2 == 0 for d in str(sq)):
        print(sq)
