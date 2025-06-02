import math

class Solution:
  def minMoves(self, nums: list[int], k: int) -> int:
    ones_indices = [i for i, num in enumerate(nums) if num == 1]
    m = len(ones_indices)

    if k == 1:
      return 0

    g = [ones_indices[j] - j for j in range(m)]

    pref_g = [0] * (m + 1)
    for i in range(m):
      pref_g[i+1] = pref_g[i] + g[i]

    min_total_moves = float('inf')

    for i in range(m - k + 1):
      current_moves = 0
      p = (k - 1) // 2
      median_val = g[i+p]

      sum_left = pref_g[i+p] - pref_g[i]
      sum_right = pref_g[i+k] - pref_g[i+p+1]
      
      offset_from_median_multiplier = (2 * p) - k + 1
      current_moves = sum_right - sum_left + (median_val * offset_from_median_multiplier)
      
      min_total_moves = min(min_total_moves, current_moves)
      
    return min_total_moves