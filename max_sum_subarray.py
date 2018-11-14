'''
def max_subarray(arr):
    cmax_sum = gmax_sum = arr[0]
    for i in range(1,len(arr)):
        cmax_sum = max(arr[i],cmax_sum+arr[i])
        if cmax_sum>gmax_sum:
            gmax_sum = cmax_sum
    return gmax_sum


print(max_subarray([1,-1,5,-2,3]))
'''

def maxSubArrayLen(arr,k):
    cur_sum =0
    cur_max = 0
    count_dict = {0:-1}
    for i in range(len(arr)):
        cur_sum+=arr[i]
        if cur_sum not in count_dict:
            print("current",cur_sum)
            count_dict[cur_sum]=i
        diff = cur_sum - k
        if diff in count_dict:
            cur_max = max(cur_max,i-count_dict[diff])
            print("cur->",i-count_dict[diff],i,count_dict[diff])
        print(diff,cur_max,'->',count_dict)
    return cur_max            
    
print(maxSubArrayLen([2,-1,-2,-1],-1))
