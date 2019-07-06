class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = []
        profit = 0
        low_price = 0
        for i in range(len(prices)):
            if i==0:
                stack.append(prices[0])
                low_price = prices[0]
            else:
                if prices[i] < low_price:
                    low_price = prices[i]
                    stack.pop()
                    stack.append(prices[i])
                else:
                    if prices[i] - low_price > profit:
                        profit = prices[i] - low_price
        return profit