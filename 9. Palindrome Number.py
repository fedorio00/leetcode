class Solution(object):
    def isPalindrome(self, x):
        answer = False
        rev_x = str(x)[::-1]
        if str(x) == rev_x:
            answer = True
        return answer

test0 = 121
test1 = -121
test2 = 10

print(Solution().isPalindrome(test0))
print(Solution().isPalindrome(test1))
print(Solution().isPalindrome(test2))