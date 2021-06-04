class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        temp = sorted(nums)
        
        j = 1
        k = 2
        x = temp [0]
        
        z = nums [k]
        
        while len(temp) != 0:
            for j in range(1,len(temp)):
                y = temp [j]
                
                for k in range(2,len(temp)):
                    z = temp[k]
