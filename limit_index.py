'''
Given a package with a weight limit limit and an array arr of item weights,
implement a function getIndicesOfItemWeights that finds two items whose sum
of weights equals the weight limit limit. Your function should return a pair
[i, j] of the indices of the item weights, ordered such that i > j. If such
a pair doesn’t exist, return an empty array.

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
'''

def get_indices_of_item_wights(arr, limit):
  if len(arr)<2:
    return []  
  for i in range(len(arr)-1,-1,-1):
    j=i-1
    diff = limit - arr[i]
    if diff in set(arr):
      while j>=0:
        if arr[j]==diff:
          break
        j-=1
      if j>i:
        return [j,i]
      else:
        return [i,j]
  return []
