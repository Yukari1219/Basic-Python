while True:
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if op == "+":
        print(a+b)
    if op == "-":
        print(a-b)
    if op == "*":
        print(a*b)
    if op == "/":
        print(a//b)
    if op == "?":
        break
    
