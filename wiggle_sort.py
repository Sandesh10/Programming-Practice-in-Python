'''
Leetcode
280 .Wiggle Sort
Given an unsorted array nums,reorder it in-place
such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4],
one possible answer is [1, 6, 2, 5, 3, 4].
'''

def wiggle_sort(num):
    index = 0
    n = len(num)
    for i in range(n):
        for j in range(n):
            if j%2!=0:
                if num[i]>=num[j]:
                    num[i],num[j] = num[j],num[i]
            else:
                if num[i]<num[j]:
                    num[i],num[j] = num[j],num[i]
    return num            
    
wiggle_sort([2,1,3,1,4,1])
