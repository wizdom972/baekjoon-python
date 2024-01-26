s = list(input())
n = 0   #0
m = 0   #1
mode = s[0]

for i in range(len(s)):
    if mode == '0' and s[i] == '1':
        mode = '1'
        n += 1
        
        #마지막에 바뀌면 1 뒤집어야 하는 횟수 +1
        if i == len(s) - 1:
            m += 1

    elif mode == '1' and s[i] == '0':
        mode = '0'
        m += 1
        #마지막에 바뀌면 0 뒤집어야 하는 횟수 +1
        if i == len(s) - 1:
            n += 1

    #0으로 연속되다가 끝나면 0 뒤집어야 하는 횟수 +1
    elif mode == '0' and i == len(s) - 1:
        n += 1

    #1으로 연속되다가 끝나면 1 뒤집어야 하는 횟수 +1
    elif mode == '1' and i == len(s) - 1:
        m += 1

print(min(n, m))