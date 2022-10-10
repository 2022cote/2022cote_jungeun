import sys

str = input()
stack = []
result = 0

for ch in str:
  
  if ch == '(' or ch == '[': # (, [ 일 경우 스택에 추가한다.
    stack.append(ch)

  elif ch == ')':
    temp = 0
    if not stack: # 빈 스택일 경우 입력이 올바르지 않은 괄호열 -> 0 출력
      print(0)
      sys.exit(0) 
    while stack:
      top = stack.pop()
      if top == '[':
        print(0)
        sys.exit(0) # 짝이 맞지 않으므로 0 출력
      elif top == '(':
        if temp == 0:
          stack.append(2)
        else:
          stack.append(temp*2)
        break
      else:
        temp += top

  elif ch == ']':
    temp = 0
    if not stack: 
      print(0)
      sys.exit(0) 
    while stack:
      top = stack.pop()
      if top == '(':
        print(0)
        sys.exit(0)
      elif top == '[':
        if temp == 0:
          stack.append(3)
        else:
          stack.append(temp*3)
        break
      else:
        temp += top

      
for res in stack:
  if res == '(' or res == '[':
    print(0)
    sys.exit(0)

print(sum(res))