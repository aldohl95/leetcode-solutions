class Solution:
  def LongestConsecutiveSequence(self, nums: List[int]) -> int:
    setList = set(nums)
    result = 0
    
    for num in setList:
      n = num
      curr = 1
      if (num - 1) not in setList:
        while (num + 1) in setList:
          curr +=1 
          n += 1
      result = max(curr, result)
    
    return result
      