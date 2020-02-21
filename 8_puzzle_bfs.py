# -*- coding: utf-8 -*-
"""8_puzzle_bfs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K2_HtOXEUmeS4TuPi8AbGbG0dhYqamKq
"""

Added PARTIAL BFS
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]

Added Bfs algorith
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]
  while f==0:
    child.clear()
    for c in range(no_of_parents):
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        break
      start_time = time.time()
      if not P in explored:
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)

      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored)

NP,o,x=run(A)

Added column wise transformation
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c
# Column converter
def column(N):
  F=copy.deepcopy(N)
  F=str(N[0])+" "+str(N[3])+" "+str(N[6])+" "+str(N[1])+" "+str(N[4])+" "+str(N[7])+" "+str(N[2])+" "+str(N[5])+" "+str(N[8])
  return F

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]
  while f==0:
    child.clear()
    for c in range(no_of_parents):
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        break
      start_time = time.time()
      if not P in explored:
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)

      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored)

NP,o,x=run(A)

Added node info
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c
# Column converter
def column(N):
  F=copy.deepcopy(N)
  F=str(N[0])+" "+str(N[3])+" "+str(N[6])+" "+str(N[1])+" "+str(N[4])+" "+str(N[7])+" "+str(N[2])+" "+str(N[5])+" "+str(N[8])
  return F

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]
  while f==0:
    child.clear()
    for c in range(no_of_parents):
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        break
      start_time = time.time()
      if not P in explored:
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)

      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored)
 
def generate_nodeinfo(o,f):
  file1 = open("NodesInfo.txt", "w")
  u=0
  j=0
  temp=1
  file1.writelines(str(1)+" "+str(0)+'\n')
  for i in range(1,x):
    file1.writelines(str(i+1)+" "+str(temp)+'\n')
    u=u+1
    if o[j]-u==0:
      j=j+1
      temp=temp+1
      u=0
  file1.close()

NP,o,x=run(A)
generate_nodeinfo(o,x)

Added text options
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c
# Column converter
def column(N):
  F=copy.deepcopy(N)
  F=str(N[0])+" "+str(N[3])+" "+str(N[6])+" "+str(N[1])+" "+str(N[4])+" "+str(N[7])+" "+str(N[2])+" "+str(N[5])+" "+str(N[8])
  return F

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  if inv%2!=0:
    print("No solution exists for this initial state")
    return 0
  else:
    print(" solution exists for this initial state",'\n',"Maximum time required to solve is 1hr 30mins",'\n',"Solving...")
  file2 = open("Nodes.txt", "w")
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]
  while f==0:
    child.clear()
    for c in range(no_of_parents):
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        file2.writelines(column(P)+ '\n')
        break
      start_time = time.time()
      if not P in explored:
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)
        file2.writelines(column(P)+ '\n')
      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored)
 
def generate_nodeinfo(o,f):
  file1 = open("NodesInfo.txt", "w")
  u=0
  j=0
  temp=1
  file1.writelines(str(1)+" "+str(0)+'\n')
  for i in range(1,x):
    file1.writelines(str(i+1)+" "+str(temp)+'\n')
    u=u+1
    if o[j]-u==0:
      j=j+1
      temp=temp+1
      u=0
  file1.close()

NP,o,x=run(A)
generate_nodeinfo(o,x)

Added generate path
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Path
def generate_path(path,N):
  file = open("nodePath.txt", "w")
  file.writelines(column(N)+ '\n')
  print(column(N))
  for p in range(len(path)):
    if path[p]=="U":
      b=BlankTileLocation(N)
      N=ActionMoveUp(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)
    elif path[p]=="D":
      b=BlankTileLocation(N)
      N=ActionMoveDown(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)
    elif path[p]=="L":
      b=BlankTileLocation(N)
      N=ActionMoveLeft(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)
    elif path[p]=="R":
      b=BlankTileLocation(N)
      N=ActionMoveRight(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c
# Column converter
def column(N):
  F=copy.deepcopy(N)
  F=str(N[0])+" "+str(N[3])+" "+str(N[6])+" "+str(N[1])+" "+str(N[4])+" "+str(N[7])+" "+str(N[2])+" "+str(N[5])+" "+str(N[8])
  return F

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  if inv%2!=0:
    print("No solution exists for this initial state")
    return 0
  else:
    print(" solution exists for this initial state",'\n',"Maximum time required to solve is 1hr 30mins",'\n',"Solving...")
  file2 = open("Nodes.txt", "w")
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]
  while f==0:
    child.clear()
    for c in range(no_of_parents):
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        file2.writelines(column(P)+ '\n')
        break
      start_time = time.time()
      if not P in explored:
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)
        file2.writelines(column(P)+ '\n')
      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored)
 
def generate_nodeinfo(o,f):
  file1 = open("NodesInfo.txt", "w")
  u=0
  j=0
  temp=1
  file1.writelines(str(1)+" "+str(0)+'\n')
  for i in range(1,x):
    file1.writelines(str(i+1)+" "+str(temp)+'\n')
    u=u+1
    if o[j]-u==0:
      j=j+1
      temp=temp+1
      u=0
  file1.close()

NP,o,x=run(A)
generate_nodeinfo(o,x)
generate_path(NP,A)

Added take input
import numpy as np
import copy
import time

#  0 1 2,3 4 5,6 7 8
#A=[6,3,8,2,4,1,0,5,7]
#A=[6,3,0,2,1,8,5,4,7]
#A=[8,6,7,2,5,4,3,0,1]
#A=[1,2,3,0,4,5,8,6,7]
#A=[1,2,3,4,0,5,7,8,6]
#A=[6,3,8,2,4,1,0,5,7]
#A=[1,0,3,4,2,5,7,8,6]

#Take input
def take_input():
  print("Enter a start node row wise (e.g 1 2 3 0 4 5 8 6 7)")
  A= [int(i) for i in input().split()]
  return A

# Find Blank
def BlankTileLocation(N):
  for i in range(9):
    if N[i]==0:
      return i

# Move up
def ActionMoveUp(b,N):
  U = copy.deepcopy(N)
  #b=BlankTileLocation(U)
  if b>2:
    U[b]=U[b-3]
    U[b-3]=0
  return U

# Move down
def ActionMoveDown(b,N):
  D = copy.deepcopy(N)
  #b=BlankTileLocation(D)
  if b<6:
    D[b]=D[b+3]
    D[b+3]=0
  return D
   
# Move left
def ActionMoveLeft(b,N):
  L = copy.deepcopy(N)
  #b=BlankTileLocation(L)
  if b!=0 and b!=3 and b!=6:
    L[b]=L[b-1]
    L[b-1]=0
  return L

# Move right
def ActionMoveRight(b,N):
  R = copy.deepcopy(N)
  #b=BlankTileLocation(R)
  if b!=2 and b!=5 and b!=8:
    R[b]=R[b+1]
    R[b+1]=0
  return R

# Path
def generate_path(path,N):
  file = open("nodePath.txt", "w")
  file.writelines(column(N)+ '\n')
  print(column(N))
  for p in range(len(path)):
    if path[p]=="U":
      b=BlankTileLocation(N)
      N=ActionMoveUp(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)
    elif path[p]=="D":
      b=BlankTileLocation(N)
      N=ActionMoveDown(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)
    elif path[p]=="L":
      b=BlankTileLocation(N)
      N=ActionMoveLeft(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)
    elif path[p]=="R":
      b=BlankTileLocation(N)
      N=ActionMoveRight(b,N)
      file.writelines(column(N)+ '\n')
      print(column(N))
      #print(N)

# Add Node
def AddNode(P,Pf,iteration,child,j):
  Pdir=Pf[9:len(Pf)]
  #print(P)
  c=0
  b=BlankTileLocation(P)
  A=ActionMoveUp(b,P)
  B=ActionMoveDown(b,P)
  C=ActionMoveLeft(b,P)
  D=ActionMoveRight(b,P)
  if P!=A:
    child=child+A+Pdir
    child.append("U")
    c=c+1
  if P!=B:
    child=child+B+Pdir
    child.append("D")
    c=c+1
  if P!=C:
    child=child+C+Pdir
    child.append("L")
    c=c+1
  if P!=D:
    child=child+D+Pdir
    child.append("R")
    c=c+1
  return c+j, child,c
# Column converter
def column(N):
  F=copy.deepcopy(N)
  F=str(N[0])+" "+str(N[3])+" "+str(N[6])+" "+str(N[1])+" "+str(N[4])+" "+str(N[7])+" "+str(N[2])+" "+str(N[5])+" "+str(N[8])
  return F

# Run BFS
def run(N):
  inv=0
  for i in range(8):
    for j in range(i,9):
      if N[i]>N[j] and N[j]!=0:
        inv=inv+1
  if inv%2!=0:
    print("No solution exists for this initial state")
    return 0
  else:
    print(" solution exists for this initial state",'\n',"Maximum time required to solve is 1hr 30mins",'\n',"Solving...")
  file2 = open("Nodes.txt", "w")
  explored=[]
  Parent= N
  child=[]
  no_of_parents=1
  no_of_childs=0
  v=0
  iteration=0
  f=0
  cn=[]
  while f==0:
    child.clear()
    for c in range(no_of_parents):
      Pf=Parent[(0+c*(9+iteration)):(iteration+9+c*(9+iteration))]
      P=Pf[0:9]
      if P==[1,2,3,4,5,6,7,8,0]:
        f=1
        explored.append(P)
        file2.writelines(column(P)+ '\n')
        break
      start_time = time.time()
      if not P in explored:
        no_of_childs,child,v=AddNode(P,Pf,iteration,child,no_of_childs)
        cn.append(v)
        explored.append(P)
        file2.writelines(column(P)+ '\n')
      else:
        cn.append(0)
    iteration+=1
    no_of_parents=int(len(child)/(9+iteration))
    Parent=copy.deepcopy(child)
    print(" Explored Nodes",len(explored))
  print(Pf[9:len(Pf)])
  return Pf[9:len(Pf)],cn,len(explored)
 
def generate_nodeinfo(o,f):
  file1 = open("NodesInfo.txt", "w")
  u=0
  j=0
  temp=1
  file1.writelines(str(1)+" "+str(0)+'\n')
  for i in range(1,x):
    file1.writelines(str(i+1)+" "+str(temp)+'\n')
    u=u+1
    if o[j]-u==0:
      j=j+1
      temp=temp+1
      u=0
  file1.close()

A=take_input()
NP,o,x=run(A)
generate_nodeinfo(o,x)
generate_path(NP,A)