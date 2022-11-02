# 풀이 참고
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
tree = []

for _ in range(N):
  start, left, right = input().split()
  tree[start] = [left, right]

# 전위 순회
def pre(start):
  if start != '.':
    print(start, end = '')
    pre(tree[start][0])
    pre(tree[start][1])

# 중위 순회
def inorder(start):
  if start != '.':
    inorder(tree[start][0])
    print(start, end = '')
    inorder(tree[start][1])

# 후위 순회
def post(start):
  if start != '.':
    post(tree[start][0])
    post(tree[start][1])
    print(start, end = '')

pre('A')
print()
inorder('A')
print()
postorder('A')