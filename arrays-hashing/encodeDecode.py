class Solution:
  def encode(self, strs: List[str]) -> str:
    encoded = ""
    for word in strs:
      enocded += str(len(word)) + "#" + word
    return encoded
  
  def decode(self, s: str) -> List[str]:
    res, i = [], 0

    while i < len(s):
      j = i 
      while s[j] != "#":
        j += 1
      lw = int(s[i:j])
      res.append[s[(j + 1):(J + 1 + lw)]]
      i = j + 1 + lw

    return res