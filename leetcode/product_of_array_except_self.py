# https://leetcode.com/problems/product-of-array-except-self

import numpy

class Solution:
    def productExceptSelf(self, nums):
        answer = []
        for i in range(len(nums)):
            tmp = nums[i]
            nums.pop(i)
            prod = numpy.prod(nums)
            answer.append(prod)
            nums.insert(i, tmp)
        return answer
