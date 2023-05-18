#PA2C Rahul Jamalapuram
#this is the AC# algorithm for 9X9 matrix
#the neighbors are the row, column, and the nearest 3X3 blocks 

row = 9
col = 9
a1 = [[0 for i in range(col)] for j in range(row)]

filename = input("Enter the Filename with txt extension ")
with open(filename) as f:
    lines = f.readlines()

for i in lines:
  a1[(int)(i.split()[0])][(int)(i.split()[1])] = [(int)(i.split()[2])]

for i in range(0,row):
  for j in range(0,col):
    if(a1[i][j] == 0):
      a1[i][j] = [1,2,3,4,5,6,7,8,9]

print("--------------")
neighbor_list = {}

#this functions creates a dictionary of nighbors for each block
def getNeighbours(i,j):
  neighbors = []
  for k in range(0, row):
    neighbors.append((i,k))
  for l in range(0,col):
    neighbors.append((l,j));
  x = (int(i/3))*3
  y = (int(j/3))*3
  for k in range(0,3):
    for l in range(0,3):
      neighbors.append((x+k,y+l))
  neighborset = set(neighbors) #Removing Duplicates
  neighborset.remove((i,j))
  return neighborset


for i in range(0,row):
  for j in range(0,col):
    neighbors = getNeighbours(i,j)
    neighbor_list[(i,j)] = neighbors

empty_queue = []

for i in range(0,row):
  for j in range(0,col):
    if(len(a1[i][j])>1):
      x = neighbor_list[(i,j)]
      for l in x:
        if(len(a1[l[0]][l[1]])==1):
          s = a1[l[0]][l[1]]
          if((a1[i][j].count(s[0]))>0):
            a1[i][j].remove(s[0])
      if(len(a1[i][j])>1):
        empty_queue.append((i,j))

#this has the queue of all non computed values or partially computed values
while(len(empty_queue)>0):
  cur = empty_queue.pop()
  x = neighbor_list[cur]
  changed=False
  for l in x:
    if(len(a1[l[0]][l[1]])==1):
      s = a1[l[0]][l[1]]
      if((a1[cur[0]][cur[1]].count(s[0]))>0):
        a1[cur[0]][cur[1]].remove(s[0])
        changed = True
      if(len(a1[cur[0]][cur[1]])>1 and changed):
        for k in x:
          empty_queue.append(k) #we have to append all the neighbors as the change in one cell can affect all its neighbors

for i in a1:
  print(i)

