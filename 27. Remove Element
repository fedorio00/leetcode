class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        answer = nums[:left]
        print(answer)
        return len(answer)


test0 = [3,2,2,3]
test1 = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(test0, 3))
print(Solution().removeElement(test1, 2))