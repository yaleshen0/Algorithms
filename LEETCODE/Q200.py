def numberIsland(graph):
	if not graph:
		return 0
	row = len(graph)
	col = len(graph[0])
	count = 0
	for i in range(row):
		for j in range(col):
			if graph[i][j] == 1:
				dfs(graph, row, col, i ,j)
				count +=1
	return count

def dfs(graph, row, col, x ,y):
	if graph[x][y] == 0:
		return
	# if its 1, we 0 it out as visited so that we wount revisit it again
	graph[x][y] = 0
	# if its not first row, we look above recursively
	if x !=0:
		dfs(graph, row, col, x-1, y)
	# if its not last row, we look above
	if x!= row-1:
		dfs(graph, row, col, x+1, y)
	# if its not first col, we look right
	if y!= 0:
		dfs(graph, row, col, x, y-1)
	if y!= col -1:
		dfs(graph, row ,col, x,y+1)

graph = [[1,1,1,1,0],
		 [1,1,0,1,0],
		 [1,1,0,0,0],
		 [0,0,0,0,0]]
print(numberIsland(graph))