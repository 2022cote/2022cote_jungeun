from collections import deque

caseCnt = int(input()) # 테스트 케이스의 수

for _ in range(caseCnt):

  N, M = map(int, input().split()) # 문서의 개수 N, 현재 Queue에서의 위치 M
  priority = 0 # 출력할 우선순위

  queue = deque(list(map(int, input().split()))) # 문서의 중요도 입력받기
  
  index = deque([False for i in range(N)]) # M번째 문서임을 표시할 index 배열 선언
  index[M] = True # M번째 문서에 표시

  while True:
    if max(queue) == queue[0]: # 첫번째 문서가 중요도가 가장 높은 문서일 때
      priority += 1 
      queue.popleft()

      if index[0]: # M번째 문서이면 출력 후 삭제
        print(priority)
        break

      else: # 그렇지 않으면 출력하지 않고 삭제
        index.popleft()

    else: # 첫번째 문서보다 중요도가 높은 문서가 있으면 조건 2를 따른다.
      queue.append(queue.popleft())
      index.append(index.popleft())