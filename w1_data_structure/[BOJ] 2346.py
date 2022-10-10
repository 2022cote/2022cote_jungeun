from collections import deque

N = int(input()) # 풍선의 개수 

queue = deque(enumerate(map(int, input().split()))) # 풍선 내부 종이의 수 리스트
result = []

while queue:
  index, val = queue.popleft()
  result.append(index+1) # 풍선의 번호는 1부터 시작

  if val > 0:
    queue.rotate(-(val-1)) # 시계 방향 회전
  else:
    queue.rotate(-val) # 시계 반대 방향 회전 

print(' '.join(map(str, result)))