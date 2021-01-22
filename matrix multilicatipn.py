import numpy

M1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

M2 = [[1,4,2],
      [3,6,0],
      [7,1,3]]
R = [[0,0,0],
     [0,0,0],
     [0,0,0]]

# iterate through rows of M1
for i in range (len(M1)):
    # iterate through columns of M2
    for j in range (len(M2[0])):
        # iterate through rows of M2
        for k in range (len(M2)):
            R[i][j] += M1[i][k] * M2[k][j]

for r in R :
    print(r)

