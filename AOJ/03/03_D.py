a, b, c = map(int, input().split())
n = 0
for x in range(a, b + 1):
    if c % x == 0:
        n += 1
print(n)
