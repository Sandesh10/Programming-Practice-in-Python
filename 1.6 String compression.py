## String compression using count of repeated characters


def func(s):
    prev = s[0]
    count = 1
    store =""
    for i in range(1,len(s)):
        if s[i]==prev:
            count+=1
        else:
            store += str(prev)
            store += str(count)
            prev=s[i]
            count = 1
    store += str(prev)
    store += str(count)        
    return(store)

##s = 'aabcccccaaabbbccc'
##print(func(s))

##       Input              Output
##'aabcccccaaabbbccc'    'a2b1c5a3b3c3'
