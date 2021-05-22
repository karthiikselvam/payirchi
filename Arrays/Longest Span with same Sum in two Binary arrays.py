# https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
"""
Input: arr1[] = {0, 1, 0, 0, 0, 0};
       arr2[] = {1, 0, 1, 0, 0, 1};
Output: 4
The longest span with same sum is from index 1 to 4.
"""

import math
def longestSpanSum(arr1,arr2):
    longsum = 0
    for i in range(len(arr1)):
        arrsum1 = 0 
        arrsum2 = 0
        for j in range(i, len(arr2)):
            arrsum1 += arr1[j]
            arrsum2 += arr2[j]
            if arrsum1 == arrsum2:
                diff = j - i + 1
                longsum = max(longsum , diff) 
        
    return longsum 

arr1 = [0, 1, 0, 0, 0, 0]
arr2 = [1, 0, 1, 0, 0, 1]
result  = longestSpanSum(arr1, arr2)
print(result)