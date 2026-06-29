class Solution:
  def ProductsOfArrayExceptItself(self, nums: List[int]) -> List[int]:
    prefix, postfix = 1, 1
    result = []

    result.append(prefix)
    for i in range(len(nums) -1):
      prefix = nums[i] * prefix
      result.append(prefix)
    
    for i in range(len(nums) -1, -1, -1):
      result[i] = postfix * nums[i]
      postfix = nums[i] * postfix
    
    return result