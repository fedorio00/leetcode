class Solution(object):
    def searchInsert(self, nums, target):
        flag = 0
        for i in nums:
            if i >= target:
                return(nums.index(i))
                break
            else:
                flag += 1
                if flag == len(nums):
                    return(len(nums))
                    break
                continue
        

print(Solution().searchInsert([1,3,5,6], 7))