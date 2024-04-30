class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # [5,  6, <0,  1,  2,  3,  4>]
        # [3,  4,  5,  6, <0,  1,  2>]
        # [2,  3,  4,  5,  6, <0,  1>]
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l = 0
        r = len(nums) - 1

        c = (l + r) // 2
        if nums[c] < nums[r]:
            if nums[c] <= target:
                l = c
            else:
                r = c - 1
        else:
            if nums[c] <= target:
                r = c
            else:
                l = c + 1

        while l < r:
            c = (l + r) // 2
            if nums[c] < target:
                l = c + 1
            else:
                r = c

        if nums[l] == target:
            return l
        else:
            return -1
