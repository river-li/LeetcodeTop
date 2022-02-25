#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l1 = head
        for _ in range(n):
            l1 = l1.next
        l2 = head
        l2_prev = l2
        while l1!=None:
            l1 = l1.next
            l2_prev = l2
            l2 = l2.next
        if l2_prev==l2:
            # 两个相等说明还没来得及往前走,需要删掉的就是head
            return head.next
        l2_prev.next = l2.next
        return head
# @lc code=end

