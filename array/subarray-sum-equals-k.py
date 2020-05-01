#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {}
        sum_dict[0] = 1
        length = len(nums)
        count = 0
        s = 0
        for i in range(length):
            s += nums[i]
            if s-k in sum_dict:
                count += sum_dict[s-k]
            sum_dict[s] = sum_dict.get(s,0) + 1
        return count