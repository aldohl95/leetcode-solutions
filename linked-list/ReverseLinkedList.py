class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def reverseListIteration(self, head: Opitonal[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev
