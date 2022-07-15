import sys

N = int(sys.stdin.readline())
a[N] = map(int, sys.stdin.readline().split())

print(min(a[N]), max(a[N]))