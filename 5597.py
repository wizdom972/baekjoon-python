attend = [0] * 31

for i in range(28):
    num = int(input())
    attend[num] = 1

result = list(filter(lambda x: attend[x] == 0, range(len(attend))))
print(*result[1:])