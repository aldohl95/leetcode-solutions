class Minstack:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    low = min(val, self.minStack[-1] if self.minStack else val)
    minStack.append(low)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()
  
  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]