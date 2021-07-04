"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def to_list(node, result=[]):
        """
        Recursive method to represent linked list chain as a python list
        :param node: ListNode chain
        :param result: List to represent chain
        :return: result
        """
        result.append(node.val)
        if node.next:
            node.to_list(node.next, result)
        return result


class Solution:
    main_node = None
    head = None

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not self.main_node:
            self.main_node = ListNode()
            self.head = self.main_node
        if l1 and l2:
            if l1.val <= l2.val:
                self.main_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                self.main_node.next = ListNode(l2.val)
                l2 = l2.next
        elif l1 and not l2:
            self.main_node.next = ListNode(l1.val)
            l1 = l1.next
        elif l2 and not l1:
            self.main_node.next = ListNode(l2.val)
            l2 = l2.next
        else:
            return self.head.next
        self.main_node = self.main_node.next
        return self.merge_two_lists(l1, l2)


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(ListNode.to_list(Solution().merge_two_lists(l1, l2)), [1, 1, 2, 3, 4, 4])
