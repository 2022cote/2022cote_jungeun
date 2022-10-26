import sys

dict = dict()
num = 0 

while True:
  str = str(sys.stdin.readline().rstrip())
  if not str: # 더 이상 입력받을 것이 없다면 반복 종료
    break
  num += 1 # 전체 나무의 수 +1
  if str in dict: # 존재하는 종일 경우 개수 +1
    dict[str] += 1
  else: # 존재하지 않을 경우 dict 에 추가
    dict[str] = 1

dict.sort()

for key, value in dict:
  print("%s %.4f" % (num, dict[key]*100/num))
  
