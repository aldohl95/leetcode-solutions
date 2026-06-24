class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    dupe = set(nums)

    if len(nums) != len(dupe):
      return True
    else:
      return False

  def hasDupOneLine(self, nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)