basketSize, iteration = map(int, input().split())

basket = [*range(basketSize + 1)]

for _ in range(iteration):
    s, e = map(int, input().split())
    rl = list(reversed(basket[s:e+1]))
    for i in range(s, e + 1):
        basket[i] = rl[i-s]

print(*basket[1:])