class Solution:
  def validParenthesis(self, s: string) -> bool:
    pair = {']':'[', '}':'{',')':'('}
    stack = []

    for sym in s:
      if sym in pair:
        if len(stack) > 0 and stack[-1] == pair[sym]:
          stack.pop()
        else:
          return False
      else:
        stack.append(sym)
    
    if len(stack) == 0:
      return True
    else:
      return False