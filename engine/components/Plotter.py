
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
		glVertex3fv(vec.toTuple() if isinstance(vec, Vector3D) else vec)
		glEnd()

	# Line
	def line(self, vec1, vec2):
		""" Draws a line from vertex `vec1` to vertex `vec2` """
		glBegin(GL_LINES)
		glVertex3fv(vec1.toTuple() if isinstance(vec1, Vector3D) else vec1)
		glVertex3fv(vec2.toTuple() if isinstance(vec2, Vector3D) else vec2)
		glEnd()

	# Triangle
	def triangle(self, vec1, vec2, vec3):
		""" Draws a triangle using vertexes `vec1`, `vec2` and `vec3` """
		glBegin(GL_TRIANGLES)
		glVertex3fv(vec1.toTuple() if isinstance(vec1, Vector3D) else vec1)
		glVertex3fv(vec2.toTuple() if isinstance(vec2, Vector3D) else vec2)
		glVertex3fv(vec3.toTuple() if isinstance(vec3, Vector3D) else vec3)
		glEnd()

	# Quadrilateral
	def quadrilateral(self, vec1, vec2, vec3, vec4):
		""" Draws a Quadrilateral using vertexes `vec1`, `vec2`, `vec3` and `vec4` """
		glBegin(GL_QUADS)
		glVertex3fv(vec1.toTuple() if isinstance(vec1, Vector3D) else vec1)
		glVertex3fv(vec2.toTuple() if isinstance(vec2, Vector3D) else vec2)
		glVertex3fv(vec3.toTuple() if isinstance(vec3, Vector3D) else vec3)
		glVertex3fv(vec4.toTuple() if isinstance(vec4, Vector3D) else vec4)
		glEnd()

	# Polygon
	def polygon(self, vecs):
		""" Draws a Polygon using vertexes in list `vecs` """
		glBegin(GL_QUADS)
		for vec in vecs:
			glVertex3fv(vec.toTuple() if isinstance(vec, Vector3D) else vec)
		glEnd()