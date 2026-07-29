class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for num in range(len(nums)-1):
            nums[num+1]+=nums[num]
        return nums
        