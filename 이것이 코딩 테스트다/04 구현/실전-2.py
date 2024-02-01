row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
steps =[(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
count = 0

location = input()

for i in range(8):
    nx = row.index(location[0]) + steps[i][0]
    ny = (int(location[1]) - 1) + steps[i][1]

    if nx >= 0 and ny >= 0 and nx <= 8 and ny <= 8:
        count += 1

print(count)