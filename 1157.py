s = input().upper()
a = sorted(list(set(s)))
l = [0]*len(a)

for i in range(len(a)):
    l[i] = s.count(a[i])

print([a[l.index(max(l))], "?"][l.count(max(l)) > 1])