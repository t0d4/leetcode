class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(nums: list[int], ans: list[int]):
            if not nums:
                res.append(ans)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :], ans + [nums[i]])

        dfs(nums, [])
        return res
