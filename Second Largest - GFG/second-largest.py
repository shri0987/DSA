class Solution:
	def print2largest(self,arr, n):
	    
	    first_max = arr[0]
	    second_max = -1
	    for i in range(len(arr)):
	        if arr[i] > first_max:
	            second_max = first_max
	            first_max = arr[i]
	            
	        elif (arr[i] < first_max) and (arr[i] > second_max):
	           second_max = arr[i]
	           
	        else:
	            continue
	        
	    return second_max


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends