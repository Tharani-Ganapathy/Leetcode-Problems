class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            i = 0
            l = len(nums)
            while i < l:
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                    l -= 1
                else:
                    i += 1
                
#             zeroCount = nums.count(0)
            
#             for i in range(zeroCount) :
#                 nums.remove(0)
            
#             nums.extend([0]*zeroCount)
            
        return nums
