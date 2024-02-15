import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input()
checkList = list(map(int, input().split()))

p = s[:m]

check = [0] * 4
check[0] = p.count('A')
check[1] = p.count('C')
check[2] = p.count('G')
check[3] = p.count('T')

isValid = 0
for i in range(4):
    if check[i] >= checkList[i]:
        isValid += 1

cnt = 0 if isValid != 4 else 1

for i in range(n - m):
    #빠지는 문자
    match s[i]:
        case 'A': 
            if check[0] == checkList[0]:
                isValid -= 1
            check[0] -= 1
        case 'C': 
            if check[1] == checkList[1]:
                isValid -= 1
            check[1] -= 1
        case 'G': 
            if check[2] == checkList[2]:
                isValid -= 1
            check[2] -= 1
        case 'T': 
            if check[3] == checkList[3]:
                isValid -= 1
            check[3] -= 1
    
    #들어오는 문자
    match s[i + m]:
        case 'A':
            check[0] += 1
            if check[0] == checkList[0]:
                isValid += 1
        case 'C': 
            check[1] += 1
            if check[1] == checkList[1]:
                isValid += 1
        case 'G': 
            check[2] += 1
            if check[2] == checkList[2]:
                isValid += 1
        case 'T': 
            check[3] += 1
            if check[3] == checkList[3]:
                isValid += 1
    
    if isValid == 4:
        cnt += 1

print(cnt)