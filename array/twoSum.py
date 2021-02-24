"""
    题目:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:

        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1]

    题目大意:
    在数组中找到 2 个数之和等于给定值的数字，结果返回 2 个数字在数组中的下标。
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            我的解题思路:
            Todo: 顺序从头开始遍历每一个元素，判断target-元素的值是否在array中，若存在则直接返回，不存在就继续下一个判断
            note: 执行用时：48 ms, 在所有 Python3 提交中击败了20.07%的用户
                  内存消耗：15 MB, 在所有 Python3 提交中击败了20.03%的用户
        """
        # for index in range(0, len(nums)-1):
        #     value = target - nums[index]
        #     if value in nums[index+1:]:
        #         index2 = nums[index+1:].index(value) + index + 1
        #         return [index, index2]

        """
            参考其他同学最优解，直接新建一个map，将target-num[i]和i填充至map中，遍历时如果发现map中有该元素，则直接返回
            执行用时：36 ms, 在所有 Python3 提交中击败了84.88%的用户
            内存消耗：14.7 MB, 在所有 Python3 提交中击败了75.37%的用户
        """
        map = {}
        for i in range(0, len(nums)):
            if nums[i] in map.keys():
                return [map.get(nums[i]), i]
            else:
                map[target - nums[i]] = i
            


if __name__ == "__main__":
    # nums = [3,3]
    # target = 6
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums=nums, target=target))

