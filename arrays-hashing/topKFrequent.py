class Solution:
  def topK(self, nums: List[int], k: int) -> List[int]:
    count = {}
    bucket = [[] for i in range(len(nums) + 1)]

    for num in nums:
      count[num] = 1 + count.get(num, 0)
    for key, val in count.items():
      bucket[val].append(key)

    result = []
    for i in range(len(bucket) -1, 0 , -1):
      for num in bucket[i]:
        result.append(i)
        if len(result) == k:
          return result
