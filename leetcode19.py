head =[1,2,3,4,5]
n=2
dummy = ListNode(0)
dummy.next = head

slow = dummy
fast = dummy

for _ in range(n + 1):
    fast = fast.next
while fast:
    slow = slow.next
    fast = fast.next
slow.next = slow.next.next
return dummy.next