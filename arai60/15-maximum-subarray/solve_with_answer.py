from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subsum, cursum = nums[0], 0
        for n in nums:
            if cursum < 0:
                # if numbers before `n` doesn't contribute, discard them
                cursum = 0
            cursum += n
            max_subsum = max(max_subsum, cursum)
        return max_subsum
