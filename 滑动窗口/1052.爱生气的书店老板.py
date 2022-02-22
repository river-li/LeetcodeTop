#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        max_value = 0
        tmp_value = 0
        n = len(customers)
        sum_value = 0
        for right in range(n):
            
            if grumpy[right]==1:
                tmp_value += customers[right]
            else:
                sum_value += customers[right]
            
            max_value=max(max_value, tmp_value)
            
            if right>=minutes-1:
                # 这里边界条件需要注意
                if grumpy[left]:
                    tmp_value -= customers[left]
                left += 1
        return max_value+sum_value

# @lc code=end

