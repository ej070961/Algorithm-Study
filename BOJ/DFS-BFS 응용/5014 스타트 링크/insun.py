from sys import stdin
import heapq
input = stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [False] * (f + 1) #각 층 방문여부 판단 리스트
q = [(0, s)] #큐 초기화, 버튼을 누른 횟수, 현재 층
visited[s] = True #시작층은 방문을 한 것임
ans = "use the stairs" #기본값으로 엘리베이터로 이동할 수 없을 때의 값을 넣어놓음
while q:
      cnt, now = heapq.heappop(q) #heap 리스트에서 가장 작은 요소를 제거하고 그 값을 반환
      # 큐에서 (버튼을 누른 횟수, 현재 층)을 꺼냄
      if now == g: #목표층 도달하면 반복 종료
            ans = cnt
            break
      if now - d > 0: #아래로 이동할 수 있는 경우
            if not visited[now - d]: #아직 방문하지 않은 층이라면
                  visited[now - d] = True #방문했다고 표시
                  heapq.heappush(q, (cnt + 1, now - d)) #q에 (cnt + 1, now - d)가 들어가는 것, q에 추가해줌
      if now + u <= f: #위로 이동할 수 있는 경우
            if not visited[now + u]: #아직 방문하지 않은 층이라면
                  visited[now + u] = True #방문했다고 표시
                  heapq.heappush(q, (cnt + 1, now + u)) 

print(ans)
