alphabet = [0 for i in range(ord("z") - ord("a") + 1)]
while True:
    try:
        contents = input().lower()
        for c in contents:
         if ord("a") <= ord(c) <= ord("z"):
            alphabet[ord(c) - ord("a")] += 1
    except EOFError:
        break

for j in range(ord("z") - ord("a") + 1):
    print(chr(j+ord("a")) + " : " + str(alphabet[j]))
