#PA2A Rahul Jamalapuram
#Implementation of AC3 Algorithm, for 3X3 matrix.
#the neighbors will be the elements in the row, column and if the element is a diagonal element the elements in the diagonal are neighbors as well.
import numpy as np

#for 3X3 matrix
row = 3
col = 3

#This matrix a has the values in the form of array of array of all possible values
a = [[0 for i in range(col)] for j in range(row)]


filename = input("Please Enter the Filename")
with open(filename) as f:
    lines = f.readlines()

#The values in the file are stored in their respective positions, the other positions are filled with [1,2,3]
for i in lines:
  a[(int)(i.split()[0])][(int)(i.split()[1])] = [(int)(i.split()[2])]

for i in range(0,row):
  for j in range(0,col):
    if(a[i][j] == 0):
      a[i][j] = [1,2,3]

#this has the dictionary of nighbors for all the positions in the matrix
neighbor_list = {}

#This Util function lists all the neighborsfor the positions of the matrix
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
    
#AC3 implementation
for i in range(0,row):
  for j in range(0,col):
    if(len(a[i][j])>1):
      x = neighbor_list[(i,j)]
      for l in x:
        if(len(a[l[0]][l[1]])==1):
          s = a[l[0]][l[1]]
          if((a[i][j].count(s[0]))>0):
            a[i][j].remove(s[0])

#printing the matrix
for i in a:
  print(i)