""" 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
# nums=[1,2,3,4,5,6,7,8,9,10]
# target=10
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i,j)
#             break
# if nums[i] + nums[j]==target:
#     print(i,j)
    
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(i, j)
                    return  
s = Solution()
s.twoSum([2, 7, 11, 15], 9)

