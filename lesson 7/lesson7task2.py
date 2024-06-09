'''
2. Задача о сумме двух элементов массива.
Напишите функцию, которая в качестве аргументов принимает массив (list) с числами
и целевое число. Функция должна возвращать индексы элементов, которые в сумме
дают целевое число.
Пример 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Объяснение: так как nums[0] + nums[1] == 9, возвращается список с индексами [0, 1].
Пример 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Пример 3:
Input: nums = [3,3], target = 6
Output: [0,1]

К сожалению, я пока не понимаю, как решить проблему со следующим вариантом инпута:

nums =
[0,4,3,0]

target =
0

Мой код возвращает [0, 0], что верну по сути но не верно по заданию
'''

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
