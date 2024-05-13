class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                length += 1
                max_length = max(length, max_length)
            else:
                while s[l] in seen:  # WRONG: items should be removed until s[r] is deleted
                    seen.remove(s[l])
                    l += 1
                length = 0
        return max_length