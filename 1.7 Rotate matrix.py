## Rotate a matrix (or image pixel) by 90 degrees.

def rotate(matrix):
    n = len(matrix)
    for row in range(((n+1)//2)):
        for col in range(row,n-1-row):
            temp = matrix[row][col]
            matrix[row][col] = matrix[n-1-col][row]
            matrix[n-1-col][row] = matrix[n-1-row][n-1-col]
            matrix[n-1-row][n-1-col] = matrix[col][n-1-row]
            matrix[col][n-1-row] = temp
    return(matrix)


##m = [[0,2,4,6,8],[-1,1,3,5,7],[-2, 0,2,4,6],[-3,-1,1,3,5],[-4,-2,0,2,4]]
##print(rotate(m))

##        Input         Rotate 90 degree      Output
## [[ 0, 2, 4, 6, 8],                     [[-4,-3,-2,-1, 0],
##  [-1, 1, 3, 5, 7],                      [-2,-1, 0, 1, 2],  
##  [-2, 0, 2, 4, 6],                      [ 0, 1, 2, 3, 4],
##  [-3,-1, 1, 3, 5],                      [ 2, 3, 4, 5, 6],
##  [-4,-2, 0, 2, 4]]                      [ 4, 5, 6, 7, 8]]
 
