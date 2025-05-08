class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cordinated = []
        found = False
        for i in range(0,len(nums)):
            
            if found:
                break 
            for j in range(0,len(nums)):
                sum = 0
                if j != i:
                    sum = nums[i]+nums[j]
                    if sum == target:
                        cordinated.append(i)
                        cordinated.append(j)
                        found = True
                        break
        return cordinated
        
        
