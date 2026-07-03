head = [1,2,3,4,5]

prev = None
curr = head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
head = prev
print(head)