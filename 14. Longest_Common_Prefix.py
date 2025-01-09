class Solution(object):
    def longestCommonPrefix(self, strs):
        answer = ""
        min_word = min(strs, key=len)
        for i in range(len(min_word)):
            for j in strs:
                if j[i] != min_word[i]:
                    return answer
            answer += min_word[i]
        return answer
                
test0 = ["flower","flow","flight"]
test1 = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(test0))
print(Solution().longestCommonPrefix(test1))