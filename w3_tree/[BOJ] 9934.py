# 풀이 참고
import sys
from collections import deque

input = sys.stdin.readline
K = int(input())
tree = list(map(int, input().split()))
ans = [[] for _ in range(K)]

def binary_(tree, level):
  if len(tree) == 1:
    ans[level].append(tree)
    return
  else:
    mid = len(tree)//2
    ans[level].append(tree[mid])
    binary_(tree[:mid], level+1)
    binary_(tree[mid+1:], level+1)

binary_(tree, 0)

for i in range(K):
  if i == 0:
    print(ans[i][0])

  else:
    print(* respi)