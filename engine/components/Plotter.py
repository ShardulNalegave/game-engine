
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

	# Triangle
	def triangle(self, vec1, vec2, vec3):
		""" Draws a triangle using vertexes `vec1`, `vec2` and `vec3` """
		glBegin(GL_TRIANGLES)
		glVertex3fv(vec1.toTuple())
		glVertex3fv(vec2.toTuple())
		glVertex3fv(vec3.toTuple())
		glEnd()

	# Quadrilateral
	def quadrilateral(self, vec1, vec2, vec3, vec4):
		""" Draws a Quadrilateral using vertexes `vec1`, `vec2`, `vec3` and `vec4` """
		glBegin(GL_QUADS)
		glVertex3fv(vec1.toTuple())
		glVertex3fv(vec2.toTuple())
		glVertex3fv(vec3.toTuple())
		glVertex3fv(vec4.toTuple())
		glEnd()

	# Polygon
	def polygon(self, vecs):
		""" Draws a Polygon using vertexes in list `vecs` """
		glBegin(GL_QUADS)
		for vec in vecs:
			glVertex3fv(vec.toTuple())
		glEnd()