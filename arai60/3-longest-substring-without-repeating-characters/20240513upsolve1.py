class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                max_length = max(r - l + 1, max_length)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        return max_length