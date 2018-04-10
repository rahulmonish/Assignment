a = [[1, 2, 3], [4, 5, 6], [1,4,5]]
nrow = len(a)
ncol = len(a[0])

print("The dimension of the matrix is ",(nrow,ncol))

count = 0
for i in a:
	for j in range(0,len(i)):
		a[count][j] = a[count][j] + 5
		a[count][j] = a[count][j] - 2
		a[count][j] = a[count][j] * 5
	count = count + 1
print(a)



