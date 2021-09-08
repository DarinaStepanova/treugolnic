import math
a = int(input())
x = [i for i in range(a)]

mmax = max(x)
abc = -1

for i in range(0, a):
    for j in range((i+1), a):
        if (mmax < x[i] + x[j]) and (x[i] < mmax + x[j]) and ( x[j] < mmax + x[i]):
            p = (x[i] + x[j] + mmax) / 2
            abc = math.sqrt(p * (p - mmax) * (p - x[i]) * (p - x[j]))

print(abc)