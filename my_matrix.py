#Class that takes care of creating a 3x3 matrix for the game
#
#
class my_matrix:

	def __init__(self):
		self.data = [[0,0,0],
		 			 [0,0,0],
		 			 [0,0,0]]


	def showMatrix(self):
		print("Matrix")
		for i in range(3):
			print(self.data[i])

	def writeMatrix(self, col, row, val):
		self.data[col][row] = val