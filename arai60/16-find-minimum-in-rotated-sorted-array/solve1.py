from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # let's find whether the left is sorted or right is sorted
        while l < r:
            c = (l + r) // 2
            if nums[c] > nums[r]:
                l = c + 1
            else:
                r = c
        return nums[l]
