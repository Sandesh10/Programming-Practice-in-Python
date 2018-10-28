def multiply(a,b):
    product = [[0 for i in range(len(b[0]))] for i in range(len(a))]  #since we need a rows and b columns
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==0:
                continue
            for k in range(len(b)):
                
                product[i][k]+= a[i][j]*b[j][k]
#                 print(product[i][k],i,j,k,a[i][j],b[j][k])
    return product

def multiply_old(a,b):
    product = [[0 for i in range(len(b[0]))] for i in range(len(a))]  #since we need a rows and b columns
    for i in range(len(a)):
        for j in range(len(b[0])):
            temp_sum = 0
            for k in range(len(a[0])):
                temp_sum+= a[i][k]*b[k][j]
            product [i][j] = temp_sum    
    return product

print(multiply([[1,0,0],[-1,1,3]],[[7,0,10,1],[1,0,0,1],[0,0,1,1]]))
print(multiply_old([[1,0,0],[-1,1,3]],[[7,0,10,1],[1,0,0,1],[0,0,1,1]]))
