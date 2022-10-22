s = list(range(1, 14))
h = list(range(1, 14))
c = list(range(1, 14))
d = list(range(1, 14))

n = int(input())
for x in range(n):
    mark, num = input(). split()
    num = int(num)
    if mark == "S":
        s.remove(num)
    elif mark == "H":
        h.remove(num)
    elif mark == "C":
        c.remove(num)
    elif mark == "D":
        d.remove(num)

[print("S", x) for x in s]
[print("H", x) for x in h]
[print("C", x) for x in c]
[print("D", x) for x in d]
