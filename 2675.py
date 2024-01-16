n = int(input())

for _ in range(n):
    m, s = input().split()
    for i in range(len(s)):
        print(s[i]*int(m), end="")
    print()