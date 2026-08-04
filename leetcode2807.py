from math import gcd
from typing import Optional
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            next_node = curr.next

            gcd_val = gcd(curr.val , next_node.val)
            new_node = ListNode(gcd_val)

            curr.next = new_node
            new_node.next = next_node

            curr = next_node
        return head