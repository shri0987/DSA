class Solution(object):
    
    def check(self, nums):
        
        def reverse(nums, i, j):
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j - 1
                
        def arraySortedOrNot(nums):
            i = 0
            j = 1
            while j < len(nums):
                if nums[j] < nums[i]:
                    return False
                else:
                    i = i + 1
                    j = j + 1
            return True
        
        i = 0
        j = 1
        
        while j < len(nums):
            
            if nums[j] < nums[i]:
                
                # Rotate the array
                
                pivot = i
                rotations = len(nums) - pivot
                reverse(nums, 0, pivot)
                reverse(nums, pivot + 1, len(nums) - 1)
                reverse(nums, 0, len(nums) - 1)
                
                if arraySortedOrNot(nums):
                    return True
                else:
                    return False
                
            else:
                i = i + 1
                j = j + 1
        
        return True
                
                
                
                
                
                
                
                
                
                
                
        
        
        