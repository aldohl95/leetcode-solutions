class Solution:
  def groupAnagrams(self, strs: List(str)) -> List[str]:
    seen = defaultdict(list)

    for word in strs:
      sorted_word = "".join(sorted(word))
      seen[sorted_word].append(word)

    return list(seen.values())