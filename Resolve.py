class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    dupe = set(nums)

    if len(dupe) < len(nums):
      return True
    return False

def validAnagram(self, s: str, t: str) -> bool:
  return Counter(s) == Counter (t)

def validPalindrome(self, s: str) -> bool:
  l , r = 0, len(s)-1

  while l < r:
    while l < r and is not s[l].isalnum():
      l += 1
    while: r > l and is not s[r].isalnum():
      r -= 1
    if s[l].lower != s[r].lower:
      return False
    
  return True
def twoSum(self, nums: List[int], target: int) ->List[]:
  seen = {}

  for i in range(len(nums)):
    complement = target - nums[i]:
    if complement in seen:
      return[seen[nums[i]] , i]
    seen[complement] = i
  
  return []

def binarySearch(self, nums: List[int], target: int) -> int:
  l, r = 0, len(nums)-1

  while l <= r:
    mid = (l + r)//2
    if nums[mid] == target:
      return mid
    if nums[mid] < target:
      l = mid + 1
    if nums[mid] > target:
      r = mid - 1
  
  return -1