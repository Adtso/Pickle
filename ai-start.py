from anytree import *
from my_matrix import *

M = my_matrix()
M.showMatrix()
B = M
M.writeMatrix(1,1,2)
M.showMatrix()
A = M
B.showMatrix()
if (B == M):
	print("iguals")