class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit = prices[i] - prices[i - 1]
                max_profit = max(max_profit, profit)
        return max_profit


solution = Solution()

print(solution.max_profit([7, 1, 0, 5, 3, 6, 4]))
