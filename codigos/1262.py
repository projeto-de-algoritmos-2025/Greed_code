import math

class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp = [0, -math.inf, -math.inf]

        for num in nums:
            prev_dp_values = list(dp)
            
            for prev_sum_val in prev_dp_values:
                if prev_sum_val == -math.inf:
                    continue
                    
                current_sum = prev_sum_val + num
                remainder = current_sum % 3
                
                dp[remainder] = max(dp[remainder], current_sum)
                
        return dp[0] if dp[0] != -math.inf else 0