listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
skipA = 2
skipB = 3
if not headA and headB:
    return None
curr1 = headA
curr2 = headB
while curr1 != curr2:
    if curr1:
        curr1 = curr1.next
    else:
        curr1 = headB
    if curr2:
        curr2 = curr2.next
    else:
        curr2 = headA
return curr2