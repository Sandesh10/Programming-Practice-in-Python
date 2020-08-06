'''
Given two strings, write a code to check if s2 is a rotation of S1
using only one call to isSubstring. 
'''

def rotation_check(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1==l2 and l1>0:
        s1 = s1+s1
        check = issubstring(s1,s2)
        print(check)
        
        
def issubstring(s1,s2):
    m = len(s1)
    n = len(s2)
    temp= False
    for i in range(m):
        count=0
        for j in range(n):
            if s1[i]==s2[j]:
                count+=1
                i+=1
                if i>=m:
                    break
        if count==n:
            temp = True
            break
        else:
            temp = False       
    return temp   


rotation_check("sandyt","tsandy")


## Output
## True
