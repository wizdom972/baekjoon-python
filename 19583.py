import sys
input = sys.stdin.readline

s, e, q = input().split()
sHour, sMinute = map(int, s.split(":"))
s = sHour * 60 + sMinute

eHour, eMinute = map(int, e.split(":"))
e = eHour * 60 + eMinute

qHour, qMinute = map(int, q.split(":"))
q = qHour * 60 + qMinute


attend = {}

while True:
    try:
        time, nickname = input().split()

        if nickname in attend:
            existTime = attend[nickname]
            existTime.append(time)
            attend[nickname] = existTime
        else:
            attend[nickname] = [time]
    except:
        break
        
result = 0

for nickname in attend:
    before = False
    end = False

    if len(attend[nickname]) >= 2:
        timeList = attend[nickname]

        for time in timeList:
            hour, minute = map(int, time.split(":"))

            tempTime = hour * 60 + minute

            if tempTime <= s:
                before = True

            if e <= tempTime <= q:
                end = True


        if before and end:
            result += 1
    else:
        continue
    
print(result)