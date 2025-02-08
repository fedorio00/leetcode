class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                result = nums[i] + nums[j]
                if result == target:
                    return [i, j]
                    
test = [3,2,4]
target = 6
print(Solution().twoSum(test, target))
