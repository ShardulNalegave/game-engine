
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *

class Plotter:

	# Init
	def __init__(self, size):
		self.size = size # Screen Size

	# Update Size
	def updateSize(self, size):
		self.size = size


	# Point
	def point(self, vec):
		""" Draws a point at vertex `vec` """
		glBegin(GL_POINTS)
		glVertex3fv(vec.toTuple())
		glEnd()

	# Line
	def line(self, vec1, vec2):
		""" Draws a line from vertex `vec1` to vertex `vec2` """
		glBegin(GL_LINES)
		glVertex3fv(vec1.toTuple())
		glVertex3fv(vec2.toTuple())
		glEnd()