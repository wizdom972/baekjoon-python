s = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in c:
    s = s.replace(a, "#")

print(len(s))