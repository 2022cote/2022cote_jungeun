import heapq # 최대 힙 자료구조 사용
import sys # 시간 초과 방지

N = int(sys.stdin.readline())
heap = []

for i in range(N):
  arr = list(map(int, input().split())) # 메모리 초과 발생
  for num in arr:
    heapq.heappush(heap, -num)

for _ in range(N-1):
  heapq.heappop(heap)

print(-1 * heapq.heappop(heap))