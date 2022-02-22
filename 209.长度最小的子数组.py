#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=math.inf

        left = 0
        n = len(nums)
        current_value = 0
        for i in range(n):
            current_value += nums[i]
            if current_value >= target:
                min_len = min(i-left+1,min_len)
                # 右指针固定，左指针右移
                while current_value>=target:
                    min_len = min(i-left+1,min_len)
                    current_value -= nums[left]
                    left += 1
        if min_len==math.inf:
            return 0
        return min_len            

        # 时间复杂度O(n)
        # 题解中给出了一个前缀和+二分查找的思路时间复杂度O(n logn)

# @lc code=end

