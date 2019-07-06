def printZigzagConcat(string, n):
	# only one row
	if(n==1):
		print(string)
		return
	# find length of string
	length = len(string)
	# create an arr of strings of all nrows
	arr =["" for i in range(length)]
	# initialize index for array of
	# strings arr[]
	row = 0
	# traverses through given string
	for i in range(length):
		# append current character
		# to current row
		arr[row] += string[i]
		# if last row is reached,
		# change direction to up
		if(row == n-1):
			down = False
		# if first row is reached,
		# change direction to down
		if(row == 0):
			down = True
		if down:
			row+=1
		else:
			row-=1
	# print concatenation of
	# all rows
	for i in range(n):
		print(arr[i], end=" ")


stri = "GEEKSFORGEEKS"
nrow = 4
printZigzagConcat(stri,nrow)