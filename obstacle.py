import sys
sys.path.remove(sys.path[1])
import cv2
import matplotlib.pyplot as plt 
import numpy as np

class Obstructions():
	def __init__(self, width, height):
		self.W = width
		self.H = height
		self.map = np.zeros([self.H, self.W], dtype=np.int8)
		self.rectangle((40,90),(60,110))
		self.circle((50,150),15)
		pass

	def rectangle(self, start, end):
		self.map[start[0]:end[0], start[1]:end[1]] = 1
		return

	def circle(self, center, radius):
		center_x, center_y = center[0], center[1]
		for i in range(center_x - radius, center_y + radius):
			for j in range(center_y - radius, center_y + radius):
				if ((i-center_x)**2 + (j - center_y)**2) <= radius**2:
					self.map[i,j] = 1
		return

	def showMap(self):
		plt.imshow(self.map, cmap="gray")	
		plt.show()

	def checkFeasibility(node):
		h,w = node[1], node[0]
		if self.map[h,w] == 1:
			return False
		elif h>self.H or w>self.W or h<0 or w<0:
			return False
		else:
			return True

	