class Solution:
  def nextPermutation(self, a: List[int]) -> None:
    n = len(a)

    # Step 1: Find the break point:
    ind = -1
    for i in range(n-2, -1, -1):
      if a[i]<a[i+1]:
        ind = i
        break
     # If break point does not exist:  
    if ind==-1:
      a.reverse()
      return a
    
    # Step 2: Find the next greater element and swap it with arr[ind]:  
    for i in range(n-1, ind, -1):
      if a[i]>a[ind]:
        a[i], a[ind] = a[ind], a[i]
        break
    
    # Step 3: reverse the right half:
    a[ind+1:] = reversed(a[ind+1:])

    return a