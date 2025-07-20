class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        
        k_temp = 0
        i = 0
        
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]==-1:
                nums[i] *= -1
                nums[i+1] *= -1
                k_temp += 1

        if nums[-1] == -1:
            nums[-1] *= -1
            k_temp+=1
        
        sum = nums[0]
        for num in nums:
            if num != sum:
                return False
            sum = num


        if k_temp < k:
            return True
        else:
            return False
            
        
newSol = Solution()
print(newSol.canMakeEqual([-1,-1,-1,1,1,1],5))
