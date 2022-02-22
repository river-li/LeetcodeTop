#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1=="":
            return True
        hash_s1 = {}
        # 各个字符出现次数
        for c in s1:
            hash_s1[c] = hash_s1.get(c,0) + 1
        hash_tmp = {}

        left = 0
        right = 0
        while right<len(s2):
            if s2[right] not in hash_s1.keys():
                # 出现了一个不在s1的字符，直接移动s1这么长
                hash_tmp.clear()
                left = right+1
                right += 1

            else:
                hash_tmp[s2[right]] = hash_tmp.get(s2[right],0) + 1
                if hash_tmp == hash_s1:
                    return True
                else:
                    right += 1
                    if right>=left+len(s1):
                        hash_tmp[s2[left]] -= 1
                        if hash_tmp[s2[left]] == 0 :
                            hash_tmp.pop(s2[left])
                        left+=1
        return False
            


# @lc code=end

