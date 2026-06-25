class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    dupe = set(nums)

    if len(dupe) < len(nums):
      return True
    return False

def validAnagram(self, s: str, t: str) -> bool:
  return Counter(s) == Counter (t)


