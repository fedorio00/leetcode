class Solution(object):
    def isValid(self, s):
        pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
        }

        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 2:
                if stack[-2] in pairs and pairs[stack[-2]] == stack[-1]:
                    stack.pop()
                    stack.pop()
        if stack == []:
            answer = True
        else:
            answer = False
        return(answer)
        

test0 = '()'
test1 = '()[]{}'
test2 = '(]'
test3 = '([])'

print(Solution().isValid(test0))
print(Solution().isValid(test1))
print(Solution().isValid(test2))
print(Solution().isValid(test3))