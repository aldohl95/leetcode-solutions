class Solution(self, prices: List[int]) -> int:
  low = float('inf')
  result = 0

  for i in range(len(prices)):
    low = min(low, prices[i])
    current = prices[i] - low
    result = max(result, current)
  return result

class SolutionSliding(self, prices: List[int]) -> int:
  low= float('inf')
  result = 0
  l,r = 0,0

  while r < len(prices):
    while r < len(prices) and prices[l] < prices[r]:
      low = min(low, prices[l])
      current = prices[r] - low
      result = max(result, current)  

    l = r
    r = l + 1
  
  return result