#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from operator import le


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 如果两个字符串的字符完全相同，两个字符串映射后的字典应该是相同的
        # 字典中键为字符，值为字符出现的次数
        idx = []
        hash_p = {}
        for c in p:
            hash_p[c] = hash_p.get(c,0) + 1
        hash_tmp = {}
        n = len(s)
        left = 0
        for i in range(n):
            hash_tmp[s[i]]=hash_tmp.get(s[i],0)+1
            if hash_tmp == hash_p:
                idx.append(left)
            
            if i>=len(p)-1:
                # 窗口定长，每次滑动左指针即可
                hash_tmp[s[left]] -= 1
                if hash_tmp[s[left]] == 0:
                    hash_tmp.pop(s[left])
                left += 1
        return idx
        # 按照滑动窗口做的，但是感觉还有优化空间，实际上每次右指针匹配到一个字符发现不在hash里面就可以直接一下子让左指针移动过来了，可以少遍历很多轮
        # 31.96% Time
        # 13.4%  Space

# @lc code=end

