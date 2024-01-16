s = input()
l = [
        ['A', 'B','C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']
    ]
t = 0

for c in s:
    for n in range(8):
        if c in l[n]:
            t = t + n + 2

t = t + len(s)
print(t)