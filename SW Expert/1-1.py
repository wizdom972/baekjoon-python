T = int(input())
for test_case in range(1, T + 1):
  result = 0
  n = int(input())

  numList = list(map(int, input().split()))
  listLen = len(numList)

  frequency = [0] * 101
    
  for i in range(listLen):
    frequency[numList[i]] += 1

  frequency.reverse()

  maxVal = max(frequency)
  result = 100 - frequency.index(maxVal)

  print(f"#{test_case} {result}")