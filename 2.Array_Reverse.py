n = int(input())
a = list(map(int, input().split()))

a.reverse()
# print(a)
for i in range (n):
  print(a[i])