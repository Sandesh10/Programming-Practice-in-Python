'''
Given a graph in matrix form, this program finds the BFS traversal
'''

def bfs_traverse(word):
    l = len(word)
    m = len(word[0])
    i,j = 0,0
    frontier = [(i,j)]
    visited = set()
    while frontier:
        current = frontier.pop(0)
        visited.add(current)
        
        neighbours = get_neighbour(current,l,m)
        for nbour in neighbours:
            if nbour in visited:
                continue
            else:
                if nbour not in frontier:
                    frontier.append(nbour)     
        print(word[current[0]][current[1]],end=" ")
        

        
def get_neighbour(current,l,m):
    output = []
    if current[0]+1<l:
        output.append((current[0]+1,current[1]))
    if current[0]-1>=0:
        output.append((current[0]-1,current[1]))
    if current[1]+1<m:
        output.append((current[0],current[1]+1))
    if current[1]-1>=0:
        output.append((current[0],current[1]-1))
    return output


bfs_traverse([[1,3,5],[2,6,7],[4,8,9]])

## Input: 1 3 5 
##        2 6 7
##        4 8 9
## Output: 1 2 3 4 6 5 8 7 9 
