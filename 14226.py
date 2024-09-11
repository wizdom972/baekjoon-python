from collections import deque

n = int(input())

visited = set()


def bfs(display_num, clip_num, time):
    visited.add((display_num, clip_num, time))
    q = deque([(display_num, clip_num, time)])

    while q:
        dn, cn, t = q.popleft()

        if dn == n:
            print(t)
            break

        # 이모티콘 삭제
        if dn - 1 >= 0:
            if (dn - 1, cn, t + 1) not in visited:
                q.append((dn - 1, cn, t + 1))
                visited.add((dn - 1, cn, t + 1))

        # 클립보드에 있는 이모티콘 붙여넣기
        if (dn + cn, cn, t + 1) not in visited:
            q.append((dn + cn, cn, t + 1))
            visited.add((dn + cn, cn, t + 1))

        # 이모티콘을 모두 복사해서 클립보드에 저장
        if (dn, dn, t + 1) not in visited:
            q.append((dn, dn, t + 1))
            visited.add((dn, dn, t + 1))


bfs(1, 0, 0)
