#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        lens = len(array)
        if lens == 1:
            return array[0]
        max_num = array[0]
        for i in range(lens):
            temp = array[i]
            if temp > max_num:
                max_num=temp
            for j in range(i+1,lens):
                temp += array[j]
                if temp > max_num:
                    max_num = temp
        return max_num

if __name__ == "__main__":
    s = Solution()
    print(s.FindGreatestSumOfSubArray([-2,-8,-1,-5,-9]))