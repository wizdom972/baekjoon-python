import sys
input = sys.stdin.readline

n = int(input())
pattern = input()
front, back = pattern.split("*")
# print(front, back)

for i in range(n):
    s = input()

    if len(s) < len(front + back):
        print("NE")

    else:
        sfront = s[:len(front)]
        sback = s[len(s)-len(back):]
        # print(sfront, sback)

        if sfront == front and sback == back:
            print("DA")
        else:
            print("NE")