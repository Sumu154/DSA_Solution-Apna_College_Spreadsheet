class Solution:
  def search(self, a: List[int], target: int) -> int:
    n = len(a)
    l,r = 0,n-1

    while l<=r:
      mid = (l+r) // 2
      if a[mid] == target:
        return mid
      # check which side is sorted
      elif a[l]<=a[mid]:       #left side sorted
        if a[l]<=target<=a[mid]:  #sorted list er majhe target thakle
          r = mid-1
        else:
          l = mid+1
      else:        #right side sorted
        if a[mid]<=target<=a[r]:
          l = mid+1
        else:
          r = mid-1
    
    return -1
