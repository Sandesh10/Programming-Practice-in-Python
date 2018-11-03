'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and
among them, there may exist one celebrity. The definition of a
celebrity is that all the other n - 1 people know him/her but he/she
does not know any of them.

Now you want to find out who the celebrity is or verify that there is
not one. The only thing you are allowed to do is to ask questions like:
"Hi, A. Do you know B?" to get information of whether A knows B. You need
to find out the celebrity (or verify there is not one) by asking as few
questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A
knows B. Implement a function int findCelebrity(n), your function should
minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.
'''

def evaluate_celebrity(space):
    def knows(x,y):
        if space[x][y]==1:
            return True
        return False
    
    stack= []
    for i in range(len(space)-1,-1,-1):
        stack.append(i)
        
    while len(stack)>1:
        A = stack.pop()
        B = stack.pop()
        if knows(A,B):
            stack.append(B)   # A can't be celebrity
        else:
            stack.append(A)   # B can't be celebrity
    celeb = stack[0]
    
    for i in range(len(space)):
        if i!= celeb:
            
            if knows(celeb,i) or not knows(i,celeb):
                return -1
    return celeb        


    
evaluate_celebrity([[0,0,1,0,1,0,1],
                    [0,0,1,0,1,0,1],
                    [0,0,0,0,1,0,0],
                    [0,0,1,0,1,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0]]
                    )
