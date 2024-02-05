credit = 0
sum = 0
score = ['F', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']

for _ in  range(20):
    _, c, s = input().split()
    
    if s == 'P':
        pass
    else:
        credit += float(c)
        tempScore = 0 if s == 'F' else (score.index(s) * 0.5 + 0.5)
        sum += (tempScore * float(c))

print(sum / credit)