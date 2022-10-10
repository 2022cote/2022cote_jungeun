n = int(input()) # 수열을 이루는 정수의 개수
stack = [] # 1~n까지의 수를 넣을 스택
result = [] # 결과 배열
flag = 1
imp = True

# 데이터를 넣기 시작

for _ in range(n):
  num = int(input()) # 맨 처음 읽을 숫자 

  while flag <= num: 
    stack.append(flag)
    result.append('+')
    flag += 1
  
  if stack[-1] == num:
    stack.pop()
    result.append('-')
  
  else:
    imp = False

if not imp:
  print('NO')
else:
  for res in result:
    print(res)
