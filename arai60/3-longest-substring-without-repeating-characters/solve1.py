class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        l = 0
        r = 1
        seen = set()
        seen.add(s[0])
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            max_len = max(r - l + 1, max_len)
            print(max_len)
            r += 1
        return max_len
