def multiply(v, G):
    result = []
    for i in range(len(G[0])): #this loops through columns of the matrix
        total = 0
        for j in range(len(v)): #this loops through vector coordinates & rows of matrix
            t = v[j] * G[j][i]
            total = total + t
        result.append(total)
    return result
v = [[1,2,3],[4,5,6],[7,8,9]]
G = [[9,8,7],[6,5,4],[3,2,1]]
print(multiply(v,G))