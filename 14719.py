h, w = map(int, input().split())
blocks = list(map(int, input().split()))

left = [blocks[0]] + [0] * (w-1)
right = [blocks[-1]] + [0] * (w-1)

left_max = left[0]
right_max = right[-1]

for i in range(w):
    if left_max < blocks[i]:
        left_max = blocks[i]

    left[i] = left_max

for i in range(w-1, -1, -1):
    if right_max < blocks[i]:
        right_max = blocks[i]

    right[i] = right_max

result = 0

for i in range(w):
    min_height = min(left[i], right[i])

    if blocks[i] >= min_height:
        continue
    else:
        result += (min_height - blocks[i])

print(result)