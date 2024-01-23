n = int(input())
w = n

for _ in range(n):
    s = input()
    al = list(set(s))

    for c in al:
        if s.find(c*s.count(c)) == -1:
            w -= 1
            break
        else:
            pass

print(w)