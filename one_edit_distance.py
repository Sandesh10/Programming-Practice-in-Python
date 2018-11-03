def one_edit_distance(s1,s2):
    count=0
    if abs(len(s1)-len(s2))>1:
        return False
#     w1 = s1 if (len(s1)>=len(s2)) else s2
#     w2 = s2 if (len(s1)>=len(s2)) else s1
    count=0
    i=0
    j=0
    while i<len(s1) and j<len(s2):
        print(s1[i],s2[j])
        if s1[i]!=s2[j]:
            if count==1:
                return False
            if len(s1)>len(s2):
                i+=1
            elif len(s2)>len(s1):
                j+=1
            else:
                i+=1
                j+=1
            count+=1
            
        else:
            i+=1
            j+=1

    if i<len(s1) or j<len(s2):
        count+=1    
    return True if count==1 else False
    
one_edit_distance("gkhb","gkshg")
