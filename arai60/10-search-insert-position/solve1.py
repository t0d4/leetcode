class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            if target < nums[c]:
                r = c - 1
            else:
                l = c + 1
        if nums[c] <= target:
            return c + 1
        else:
            return c
