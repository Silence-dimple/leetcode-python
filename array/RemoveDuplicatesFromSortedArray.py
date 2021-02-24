"""
    题目:
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Example1:
    Given nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the returned length.

    Example2:
    Given nums = [0,0,1,1,1,2,2,3,3,4],
    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
    It doesn't matter what values are set beyond the returned length.

    说明:
    Confused why the returned value is an integer but your answer is an array?
    Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
    Internally you can think of this:

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeElement(nums, val);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }


    题目大意:
    给定一个有序数组 nums，对数组中的元素进行去重，使得原数组中的每个元素只有一个。最后返回去重以后数组的长度值。
"""

from typing import List


class Solution(object):
    """
        解题思路：
        todo: 注意这是一个有序的数组，题目不允许使用额外的数组空间
    """
    def removeDuplicates(self, nums: List[int]) -> int:

        # 解法一：
        """
            直接从开始遍历数组，若找到与当前值不相等时直接覆盖原有的值即可
            执行用时：56 ms, 在所有 Python3 提交中击败了33.61%的用户
            内存消耗：15.8 MB, 在所有 Python3 提交中击败了23.24%的用户
        """
        # if len(nums) == 0:
        #     return 0
        # i, j = 0, 0
        # while i < len(nums)-1:
        #     while nums[i] == nums[j]:
        #         j += 1
        #         if j == len(nums):
        #             return i + 1
        #     nums[i + 1] = nums[j]
        #     i += 1
        # print(nums)
        # return i + 1

        # 解法二：
        """
        执行用时：40 ms, 在所有 Python3 提交中击败了89.65%的用户
        内存消耗：16 MB, 在所有 Python3 提交中击败了5.03%的用户
        """
        # temp = sorted(list(set(nums))) # 40ms
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # return len(temp)


        # 解法三
        """
        (思路相同，但是代码更简洁)
        执行用时：44 ms, 在所有 Python3 提交中击败了77.34%的用户
        内存消耗：15.6 MB, 在所有 Python3 提交中击败了68.48%的用户
        """
        i = 1
        for j in range(len(nums)):
            if j > 0 and nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i





if __name__ == '__main__':
    # nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1, 1, 2, 2, 3, 4, 5]
    result = Solution().removeDuplicates(nums=nums)
    print(result)
