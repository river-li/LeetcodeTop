#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 这个思路相当于是每一次合并一个链表进来，直到所有的链表都被合并进去了
    # 时间复杂度O(k2n)
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if len(lists)==0:
    #         return None
    #     flag = True
    #     while flag:
    #         list1 = lists.pop()
    #         if len(lists)==0:
    #             return list1
    #         list2 = lists.pop()
    #         lists.append(self.mergeTwoLists(list1,list2))
            
    # 比上面稍微优化了一点
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists,left,right):
        if left==right:
            return lists[left]
        mid = (left+right)//2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, list1,list2):
        if list1==None:
            return list2
        if list2==None:
            return list1
        
        result = ListNode()
        p = result
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                p.next = list1
                p = p.next
                list1 = list1.next
            else:
                p.next = list2
                p = p.next
                list2 = list2.next
        if list1==None:
            p.next = list2
        elif list2==None:
            p.next = list1
        return result.next
# @lc code=end

