#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_value = 0
        left = 0
        n = len(nums)
        lookup = set()
        current_value = 0

        for right in range(n):
            # 右指针
            current_value += nums[right]
            if nums[right] not in lookup:
                lookup.add(nums[right])
                max_value = max(max_value, current_value)

            else:
                while nums[right] in lookup:
                    lookup.remove(nums[left])
                    current_value -= nums[left]
                    left = left + 1
                lookup.add(nums[right])
                
        return max_value
# @lc code=end

