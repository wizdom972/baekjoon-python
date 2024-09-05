n, m, h = map(int, input().split())

ladder = [[] for _ in range(h+1)]
for _ in range(m):
    h, line = map(int, input().split())
    ladder[h].append(line)

def start_game(ladder):
    for i in range(1, n+1):
        result = i

        for j in range(1, h+1):
            if result in ladder[j]:
                result += 1
                continue
            elif result - 1 >= 1 and result - 1 in ladder[j]:
                result -= 1
                continue
        