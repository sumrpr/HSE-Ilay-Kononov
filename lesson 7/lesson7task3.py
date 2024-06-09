'''
1. Задача о палиндроме.
Напишите функцию, которая будет принимать в себя тип данных int (число) и
возвращать тип bool, если переданное число является палиндромом.
Палиндром — слово, фраза или символы, которые одинаково читаются слева направо
и справа налево.
Пример 1:
Input: x = 121
Output: true
Объяснение: так как число читается одинаково в обе стороны, то функция вернёт True.
Пример 2:
Input: x = -121
Output: false
Пример 3:
Input: x = 10
Output: false
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        g = len(xstr)
        f = []
        for i in range(len(xstr)):
            f.append(xstr[g - 1])
            g -= 1
        try:
            if (int(''.join(f)) == x):
                return(True)
            else:
                return(False)
        except:
            return(False)
