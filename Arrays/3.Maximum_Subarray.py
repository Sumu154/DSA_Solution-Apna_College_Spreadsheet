import math

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    maxSum = -math.inf
    currSum = 0

    for val in nums:
      currSum += val
      maxSum = max(maxSum, currSum)
      if currSum < 0:
        currSum = 0

    return maxSum


        