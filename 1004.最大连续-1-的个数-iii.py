#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        hash_tmp = {0:0,1:0}
        max_one = 0
        left = 0
        n = len(nums)
        for right in range(n):
            hash_tmp[nums[right]] = hash_tmp.get(nums[right],0) + 1
            while hash_tmp[0] > k:
                hash_tmp[nums[left]] -= 1
                left += 1

            max_one = max(max_one,right-left+1)
        return max_one
        # 还和之前一样用字典存储数字个数有点复杂了
        # 这里题解给的思路是可以使用 1-nums[right]这样来表示是否是1
        # 直接转化为了求sum，算起来更快

# @lc code=end

