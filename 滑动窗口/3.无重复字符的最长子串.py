#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lookup = set()
        n = len(s)
        maxv = 0
        curv = 0
        for i in range(n):
            curv += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curv -= 1
            if curv>maxv:
                maxv=curv
            lookup.add(s[i])
        return maxv
        # 滑动窗口，右边的指针就是外层循环不用管
        # 在出现重复字符的时候左边的指针逐个向右移动，由内层循环控制



# @lc code=end

