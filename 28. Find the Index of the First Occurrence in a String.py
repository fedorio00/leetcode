class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return(haystack.index(needle))
        else:
            return(-1)

print(Solution().strStr("sadbutsad","sad"))
print(Solution().strStr("leetcode","leeto"))