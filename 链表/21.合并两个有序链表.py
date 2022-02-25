#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1
        
        result = ListNode()
        p = result
        l1 = list1
        l2 = list2
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                p.next=l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = p.next
        if l2!=None:
            p.next = l2
        if l1!=None:
            p.next = l1
        return result.next
# @lc code=end

