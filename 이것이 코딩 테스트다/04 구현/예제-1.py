location = [1, 1]
n = int(input())
route = list(input().split())

for i in range(len(route)):
    if location[0] > 1 and route[i] == 'U':
        location[0] -= 1
    elif location[0] < n and route[i] == 'D':
        location[0] += 1
    elif location[1] > 1 and route[i] == 'L':
        location[1] -= 1
    elif location[1] < n and route[i] == 'R':
        location[1] += 1

print(*location)