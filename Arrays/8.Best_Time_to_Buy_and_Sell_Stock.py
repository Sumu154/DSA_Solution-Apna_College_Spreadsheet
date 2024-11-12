class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    buy_price = prices[0]
    ans=0

    for i in prices[1:]:
      buy_price = min(buy_price, i)

      ans = max(ans, i-buy_price)

    return ans


                                                                                                      