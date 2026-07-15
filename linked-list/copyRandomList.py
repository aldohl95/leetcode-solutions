class Soluton:
  def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    copyToOld = {None: None}
    

    cur = head
    while cur:
      copy = Node(cur.val)
      copyToOld[cur] = copy
      cur = cur.next

    cur = head
    while Cur:
      copy = copyToOld[cur]
      copy.next = copyToOld[cur.next]
      copy.random = copyToOld[cur.random]
      cur.next
    return copyToOld[head]


