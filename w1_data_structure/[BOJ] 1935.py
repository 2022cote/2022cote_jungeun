N = int(input()) # 피연산자의 개수
exp = input() 
stack = []
num = [] # 피연산자 대응 값을 저장

for _ in range(N):
  num.append(int(input()))


# 문자일 경우 스택에 push, 숫자일 경우 pop 수행
for ch in exp:
  
  if ch.isalpha(): # 알파벳일 경우
    stack.append(num[ord(ch)-ord('A')]) # 해당 인덱스의 값을 추가한다. 

  else:
    firstOper = stack.pop()
    secondOper = stack.pop()

    if ch == '+':
      stack.append(secondOper+firstOper)
    elif ch == '-':
      stack.append(secondOper-firstOper)
    elif ch == '*':
      stack.append(secondOper*firstOper)
    elif ch == '/':
      stack.append(secondOper/firstOper)

print(format(stack.pop(), ".2f"))
