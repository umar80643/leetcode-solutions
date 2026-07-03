list1 = [1,2,4]
list2 = [1,3,4]
head1 = list1
head2 = list2
if head1 is None:
    return head2
if head2 is None:
    return head1
f_head = None
f_tail = None
while head1 is not None and head2 is not None:
    if head1.val < head2.val:
        if f_head == None:
            f_head = head1
            f_tail = head1
        else:
            f_tail.next = head1
            f_tail = head1

        head1 = head1.next

    else:
        if f_head == None:
            f_head = head2
            f_tail = head2
        else:
            f_tail.next = head2
            f_tail = head2
        head2 = head2.next
if head1 is not None:
    f_tail.next = head1
if head2 is not None:
    f_tail.next = head2
return f_head