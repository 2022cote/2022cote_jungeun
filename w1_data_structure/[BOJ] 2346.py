from collections import deque

N = int(input()) # 풍선의 개수 

# 풍선의 index 값은 보존되어야 함 -> enumerate 함수 사용
queue = deque(enumerate(map(int, input().split()))) # 풍선 내부 종이의 수 리스트
result = []

while queue:
  index, val = queue.popleft()
  result.append(index+1) # 풍선의 번호는 1부터 시작

  if val > 0:
    queue.rotate(-(val-1)) # -(양수) = 음수 -> rotate 왼쪽으로
  else:
    queue.rotate(-val) # -(음수 값) = 양수 -> rotate 오른쪽

print(' '.join(map(str, result)))