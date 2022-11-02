import sys

input = sys.stdin.readline
N = int(input())

tree = [-1 for i in range(N+1)]

for _ in range(N-1):
    arr = list(map(int, input().split()))
    for num in arr:
        if tree[num] < 1:
            tree[num] += 1

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        tree[k]==1?print('yes'):print('no')
    else:
        print('yes')