A = []
print("Enter the elements fo the first matrix")
for i in range(0,3):
    A.append([])
    for j in range(0,3):
        A[i].append(int(input()))

B = []
print("Enter the elements fo the second matrix")
for i in range(0,3):
    B.append([])
    for j in range(0,3):
        B[i].append(int(input()))

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("The result is: ",result)