#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        left = 0
        temp_cost = 0
        cost_array = []
        for right in range(len(s)):
            cost_array.append(abs(ord(s[right])-ord(t[right])))
            temp_cost += cost_array[right]
            if temp_cost > maxCost:
                while temp_cost > maxCost:
                    temp_cost -= cost_array[left]
                    left += 1
            max_len = max(max_len,right-left+1)
        return max_len

# @lc code=end

