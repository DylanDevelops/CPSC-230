class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in found:
                return [found[complement], i]
            found[num] = i




# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         found = [0, 0]

#         for i in nums:
#             for x in nums:
#                 if i + x == target and nums.index(i) != nums.index(x):
#                     found[0] = nums.index(i)
#                     found[1] = nums.index(x)
#                     return found