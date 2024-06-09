class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            low = 0
            high = len(nums) - 1
            mid = len(nums) // 2
            while nums[mid] != target - i and low <= high:
                if target - i > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2

            if low > high:
                continue
            else:
                return(nums.index(i), mid)
                break
