# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        head2 = head
        while head2.next != None:
            head2 = head2.next
        last = head2

        head3 = head
        while head3.next.next != None:
            if head3.next.val % 2 == 0:
                last.next = head3.next
                head3.next = head3.next.next
            head3 = head3.next
        return head
