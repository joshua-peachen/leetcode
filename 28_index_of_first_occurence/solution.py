class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for ind in range(len(haystack)):
            substr = haystack[ind:ind+len(needle)]
            if substr == needle:
                return ind
        return -1

if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("a", "a", 0),
        ("ab", "b", 1),
        ("a", "b", -1),
        ("ab", "ab", 0)
    ]
    for haystack, needle, expected in test_cases:
        actual = sol.strStr(haystack, needle)
        print(f'{haystack = }, {needle = }, {expected == actual}')