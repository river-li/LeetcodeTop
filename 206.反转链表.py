#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 理想解法应该是一共需要申请两个节点暂存
# 之后每一次迭代下一个节点时都让next指向其前一个节点
# 这样的时间复杂度O(N)空间复杂度O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        pointer = head.next
        result = ListNode(val=head.val, next=None)
        
        result_pointer = result
        while pointer!=None:
            result = ListNode(val=pointer.val, next=result_pointer)
            result_pointer = result
            pointer = pointer.next

        return result


# @lc code=end

