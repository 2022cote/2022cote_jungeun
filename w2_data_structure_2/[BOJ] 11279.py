import heapq # 최대 힙 자료구조 사용
import sys # 시간 초과 방지

heap = []
N = int(sys.stdin.readline())

for _ in range(N):
  val = int(sys.stdin.readline())

  if val > 0:
    heapq.heappush(heap, -val) # 최대 힙이므로, 부호를 바꿔서 저장한다
  elif val == 0:
    if len(heap)==0:
      print(0)
    else:
      print(-1 * heapq.heappop(heap)) # 출력 시 부호를 바꾸어 출력한다
  