class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = 0
        
        if len(nums) == 1:
            return nums
    
        while j < len(nums):
            
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]   # Swap the elements
                i = i + 1
                j = j + 1
                
            elif nums[i] == 0 and nums[j] == 0:
                j = j + 1
            
            else:
                i = i + 1
                j = j + 1
        
        return nums  
                
            
                
            
                
            
            