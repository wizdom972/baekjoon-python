for i in range(10):
  buildingNum = int(input())
  buildings = list(map(int, input().split()))

  result = 0

  for j in range(2, buildingNum - 2):
    minGap = buildings[j] - max(buildings[j-2], buildings[j-1], buildings[j+1], buildings[j+2])

    if minGap > 0:
      result += minGap

  print(f"#{i+1} {result}")
