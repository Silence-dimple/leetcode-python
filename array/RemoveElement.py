"""
    题目:
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn’t matter what you leave beyond the new length.

    Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2]
    Explanation: Your function should return length = 2, with the first two elements of nums being 2.
    It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

    Example2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3]
    Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.

    题目大意:
    给定一个数组 nums 和一个数值 val，将数组中所有等于 val 的元素删除，并返回剩余的元素个数。
"""
from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)
        return j



if __name__ == "__main__":
    # nums = [0,1,2,2,3,0,4,2]
    # target = 2
    nums = [3, 2, 2, 3]
    target = 3
    result = Solution().removeElement(nums=nums, val=target)
    print(result)
