#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        以下解法复杂度过高，在遇到大测试用例时超时
        left = 0
        n = len(nums)
        maxv=sum(nums[:k])
        for i in range(n-k+1):
            tmpv = sum(nums[i:i+k])
            if tmpv>maxv:
                maxv=tmpv
        return maxv/k
        """

        # 滑动窗口，总的来说只需要遍历一次
        left = 0
        n = len(nums)
        sumv=0
        maxv=-math.inf
        for i in range(n):
            sumv+=nums[i]
            if i-left+1==k:
                maxv=max(maxv,sumv)
            if i>=k-1:
                sumv -= nums[left]
                left += 1
        return maxv/k

# @lc code=end

