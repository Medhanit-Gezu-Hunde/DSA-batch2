class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        result=[num for num in nums if num !=0] #creates the result in array
        result.extend([0]*(n-len(result))) #appends zeros to the end
        return result
        
