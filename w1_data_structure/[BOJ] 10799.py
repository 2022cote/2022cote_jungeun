data = input() 
stack = []
result = 0

for i in range(len(data)):
  # 오류 케이스는 없다고 가정한다.
 
  if data[i] == '(': # '(' 일 경우 스택에 삽입
    stack.append('(')
  else:
    # 바로 직전의 값이 '(' 라면, 레이저에 해당한다. 
    if data[i-1] == '(':
      stack.pop()
      result += len(stack)
    else:
      # 바로 직전 값이 ')' 라면, 해당 막대기의 끝
      stack.pop()
      result += 1
  
print(result)
# test