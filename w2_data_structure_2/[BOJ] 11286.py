import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -1*num) # 최소 힙은 그대로 적용한다
    else:
        if num == 0:
            print(-1 * heapq.heappop(heap)[1]) 
        else:
            print(0)