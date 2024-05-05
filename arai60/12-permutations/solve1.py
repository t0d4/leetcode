import itertools


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(itertools.permutations(nums, len(nums)))
