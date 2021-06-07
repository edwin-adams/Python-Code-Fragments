class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        nums.sort()
        
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
                
            leftPtr, rightPtr = i + 1 , len(nums) - 1 #left and right pointers on input array
            while leftPtr < rightPtr:
                triplet = x + nums[leftPtr] + nums[rightPtr]
                if triplet > 0:
                    rightPtr -= 1
                elif triplet < 0:
                    leftPtr += 1
                else:
                    triplets.append([x, nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    while nums[leftPtr] == nums[leftPtr -1] and leftPtr < rightPtr:
                        leftPtr += 1
        
        return triplet
