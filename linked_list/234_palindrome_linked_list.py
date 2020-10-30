# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def reverse(root):
            temp = None
            prev = None
            curr = root

            if not curr:
                return curr

            while curr.next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            curr.next = prev
            return curr

        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        head1 = head

        head2 = reverse(head2)

        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next

        return True
