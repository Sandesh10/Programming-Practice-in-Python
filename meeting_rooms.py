'''
Given an array of meeting time intervals consisting of start and
end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number
of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

'''

def check_meeting(mlist):
    l = len(mlist)
    if l==0:
        return 0
    mlist.sort(key=lambda mlist:mlist[0])
    count=1
    for i in range(l-1):
        if mlist[i][1]<=mlist[i+1][0]:
            continue
        else:
            count+=1
    return count        
        
    
print(check_meeting([[20,30],[20, 30],[26, 27],[28, 30]]))
