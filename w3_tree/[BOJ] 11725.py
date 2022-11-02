import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

tree = [[] for _ in range(N+1)]
visited = [[0] for _ in range(N+1)] 

# BFS 풀이
def bfs(node):
  q = deque()
  q.append(node)
  visited[node] = 0

  while q:
    item = q.popleft()
    for n in tree[item]:
      if visited[n] == 0:
        q.append(n)
        visited[item] = n
    
for _ in range(N-1):
  node1, node2 = map(int, sys.stdin.readline().split())
  tree[node1].append(node2)
  tree[node2].append(node1)

bfs(1)

# 오류 발생..(TypeError)
for vis in visited:
  print(vis)

