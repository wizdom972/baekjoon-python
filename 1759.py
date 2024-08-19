from itertools import combinations

l, c = map(int, input().split())
chars = input().split()

chars.sort()

vowel = ["a", "e", "i", "o", "u"]
for word in combinations(chars, l):
    vNum = 0
    cNum = 0

    for i in range(len(word)):
        if word[i] in vowel:
            vNum += 1
    
    cNum = len(word) - vNum

    if vNum >= 1 and cNum >= 2:
        print("".join(word))
