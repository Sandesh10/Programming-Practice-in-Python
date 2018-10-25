def dfs_traversal(word):
    visited = [[False for i in range(len(word[0]))]]* len(word)
    for i in range(len(word)):
        for j in range(len(word[0])):
            print(i,j,visited)
            if visited[i][j]==False:
                dfs_helper((i,j), word,visited)
            
def dfs_helper(current, word, visited):
    
    visited[current[0]][current[1]] = True
    print("current",current, visited)
    print(word[current[0]][current[1]])
    neighbour = get_neighbour(current,len(word),len(word[0]))
    
    for nbour in neighbour:
        print(nbour, end=",")
        if visited[nbour[0]][nbour[1]]==False:
            dfs_helper(nbour,word,visited)

def get_neighbour(current,l,m):
    output = []
    if current[0]+1<l:
        output.append((current[0]+1,current[1]))
    if current[1]+1<m:
        output.append((current[0],current[1]+1))
        
#   You don't have to compute the next two neighbours as
#   they have already been visited. I am showing this 
#   to explain it in general. 
    if current[0]-1>=0:
        output.append((current[0]-1,current[1]))
    if current[1]-1>=0:
        output.append((current[0],current[1]-1))
    return output    
        
dfs_traversal([[1,3,5],[2,6,7],[4,8,9]])
