def findMinDiff(a, m):
  n = len(a)
  a.sort()

  minDiff = float('inf')
  for i in range(0, n-m+1):
    diff = a[i+m-1]-a[i]
    minDiff = min(minDiff, diff)

  return minDiff


if __name__ == "__main__":
  n, m = map(int, input().split())
  a = list(map(int, input().split()))

  print(findMinDiff(a, m))
