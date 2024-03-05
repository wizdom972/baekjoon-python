import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

data.sort()

for t in test:
    start = 0
    end = n - 1
    flag = False

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == t:
            print(1)
            flag = True
            break
        elif data[mid] < t:
            start = mid + 1
        else:   #data[mid] > t
            end = mid - 1

    if flag == False:
        print(0)