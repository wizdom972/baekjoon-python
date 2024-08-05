for i in range(10):
  dumpNum = int(input())
  box = list(map(int, input().split()))

  for j in range(dumpNum):
    minIndex = box.index(min(box))
    maxIndex = box.index(max(box))

    box[minIndex] += 1
    box[maxIndex] -= 1

  minHeight = min(box)
  maxHeight = max(box)

  print(f"#{i+1} {maxHeight-minHeight}")