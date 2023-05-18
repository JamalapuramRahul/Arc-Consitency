#PA2B Rahul Jamalapuram
#This has the AC3 implementation for which the backtracking for the output
import numpy as np

#this is for 3X3 matrix
row = 3
col = 3
a = [[0 for i in range(col)] for j in range(row)]

filename = input("enter the filename with .txt extension ")
with open(filename) as f:
    lines = f.readlines()


for i in lines:
  a[(int)(i.split()[0])][(int)(i.split()[1])] = [(int)(i.split()[2])]

for i in range(0,row):
  for j in range(0,col):
    if(a[i][j] == 0):
      a[i][j] = [1,2,3]

neighbor_list = {}


def getNeighbours(i,j):
  neighbors = []
  for k in range(0, row):
    neighbors.append((i,k))
  for l in range(0,col):
    neighbors.append((l,j));
  if(i==j):
    for l in range(0, row):
      if(i!=l):
        neighbors.append((l,l))
  neighborset = set(neighbors)
  neighborset.remove((i,j))
  return neighborset

for i in range(0,row):
  for j in range(0,col):
    neighbors = getNeighbours(i,j)
    neighbor_list[(i,j)] = neighbors
    
for i in range(0,row):
  for j in range(0,col):
    if(len(a[i][j])>1):
      x = neighbor_list[(i,j)]
      for l in x:
        if(len(a[l[0]][l[1]])==1):
          s = a[l[0]][l[1]]
          if((a[i][j].count(s[0]))>0):
            a[i][j].remove(s[0])

#this is the backtracking algorithm
#the count of for each value is stored as global count
count = 0

#this is the util function that returns if the number is present in the row diagonal or the column
def value_fits(a3,row,col,number):
  for i in range(0,3):
    if((a3[row][i]) == [number]):
      return False

  for i in range(0,3):
    if((a3[i][col]) == [number]):
      return False

  if(row == col):
    for i in range(3):
      if(i != row):
        if((a3[i][i]) == [number]):
          return False
  return True

#the util function backtracking
def backtrack(a3,row,col):
  global count
  if(row ==2 and col == 3):
    return True

  if col == 3:
        row =row + 1
        col = 0

  if(len(a3[row][col]) == 1):
    return backtrack(a3, row, col + 1)


  for i in range(1,4):
    if(value_fits(a3,row,col,i)):
      prev = a3[row][col]
      (a3[row][col])= [i]
      count+=1
      if backtrack(a, row, col + 1):
        return True
      a3[row][col] = prev
  return False

a3 = a.copy()
if(backtrack(a3, 0, 0)):
  for i in a3:
    print(i)

#Prints the Count of for each value
print("Count of for each value is",count)

