N,M = map(int, input().split())
count = 0
data = []

for i in range(N):
  data.append(input())

for i in range(M):
  string = input()
  if string in data: # 새로운 input 값이 집합 내에 존재한다면 count+=1
    count += 1 

print(count)