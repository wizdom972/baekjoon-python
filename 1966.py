from collections import deque

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))

    order = 0

    while q:
        priority = q[0]
        flag = False

        for document in list(q)[1:]:
            if document > priority:
                q.append(q.popleft())
                
                m -= 1
                if  m < 0:
                    m += len(q)
                
                flag = True

                break

        if flag:
            continue

        q.popleft()
        
        m -= 1        
        order += 1

        if m < 0:
            break

    print(order)
