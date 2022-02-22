#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 这个题目可以转化成滑动窗口，滑动的是中间的值，长度len(cardPoint)-k
        # 使得这个数组和最小
        start=0
        l = len(cardPoints) - k
        sum_value = 0
        tmp_value = 0
        min_value = math.inf

        if l==0:
            return sum(cardPoints)

        for end in range(len(cardPoints)):
            sum_value += cardPoints[end]
            tmp_value += cardPoints[end]

            # 由于窗口固定长度，直接在大于l之后都滑动即可
            if end>=l-1:
                min_value = min(min_value, tmp_value)
                # 这句求最小值如果在上面写会没办法保证窗口长度
                tmp_value -= cardPoints[start]
                start += 1
        return sum_value - min_value


# @lc code=end

