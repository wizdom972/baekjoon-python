n = int(input())
l = list(map(int, input().split()))

avg = sum(l)/max(l)*100/n
print(avg)