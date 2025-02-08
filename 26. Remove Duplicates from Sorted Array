class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while len(nums) - 1 > i:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return(nums)

test0 = [1,1,2]
test1 = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(test0))
print(Solution().removeDuplicates(test1))