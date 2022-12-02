class Solution(object):
    def maxProduct(self, nums):
        
        first_max = -1
        second_max = -1
        
        for i in range(len(nums)):
            
            if (nums[i] >= first_max):
                second_max = first_max
                first_max = nums[i]
                
            elif (nums[i] <= first_max) and (nums[i] >= second_max):
                second_max = nums[i]
                
            else:
                continue
        
        return (first_max - 1) * (second_max - 1)
        