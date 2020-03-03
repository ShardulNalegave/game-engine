
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import *


class Box:
	def __init__(self, name, origin, scale, plotter):
		self.name = name
		self.origin = origin
		self.plotter = plotter
		self.scale = scale
		self.shiftVal = Vector3D(0, 0, 0)
		self.rotateOn = Vector3D(0, 0, 0)
		self.rotated = 0
		self.rotateDegrees = 0

	def rotate(self, deg, rotateOn):
		self.rotateOn = rotateOn
		self.rotateDegrees = deg

	def __getData(self):
		verticies = {
			"back": {
				"top-left": ((self.origin.x + self.shiftVal.x) - (self.scale.x/2), (self.origin.y + self.shiftVal.y) + (self.scale.y/2), (self.origin.z + self.shiftVal.z) - (self.scale.z/2)),
				"top-right": ((self.origin.x + self.shiftVal.x) + (self.scale.x/2), (self.origin.y + self.shiftVal.y) + (self.scale.y/2), (self.origin.z + self.shiftVal.z) - (self.scale.z/2)),
				"bottom-right": ((self.origin.x + self.shiftVal.x) + (self.scale.x/2), (self.origin.y + self.shiftVal.y) - (self.scale.y/2), (self.origin.z + self.shiftVal.z) - (self.scale.z/2)),
				"bottom-left": ((self.origin.x + self.shiftVal.x) - (self.scale.x/2), (self.origin.y + self.shiftVal.y) - (self.scale.y/2), (self.origin.z + self.shiftVal.z) - (self.scale.z/2))
			},
			"front": {
				"top-left": ((self.origin.x + self.shiftVal.x) - (self.scale.x/2), (self.origin.y + self.shiftVal.y) + (self.scale.y/2), (self.origin.z + self.shiftVal.z) + (self.scale.z/2)),
				"top-right": ((self.origin.x + self.shiftVal.x) + (self.scale.x/2), (self.origin.y + self.shiftVal.y) + (self.scale.y/2), (self.origin.z + self.shiftVal.z) + (self.scale.z/2)),
				"bottom-right": ((self.origin.x + self.shiftVal.x) + (self.scale.x/2), (self.origin.y + self.shiftVal.y) - (self.scale.y/2), (self.origin.z + self.shiftVal.z) + (self.scale.z/2)),
				"bottom-left": ((self.origin.x + self.shiftVal.x) - (self.scale.x/2), (self.origin.y + self.shiftVal.y) - (self.scale.y/2), (self.origin.z + self.shiftVal.z) + (self.scale.z/2))
			}
		}
		edges = [
			# Back face
			(verticies["back"]["top-left"], verticies["back"]["top-right"]),
			(verticies["back"]["top-left"], verticies["back"]["bottom-left"]),
			(verticies["back"]["bottom-left"], verticies["back"]["bottom-right"]),
			(verticies["back"]["top-right"], verticies["back"]["bottom-right"]),
			# Front face
			(verticies["front"]["top-left"], verticies["front"]["top-right"]),
			(verticies["front"]["top-left"], verticies["front"]["bottom-left"]),
			(verticies["front"]["bottom-left"], verticies["front"]["bottom-right"]),
			(verticies["front"]["top-right"], verticies["front"]["bottom-right"]),
			# Z-axis connecters (connecting both squares)
			(verticies["back"]["top-left"], verticies["front"]["top-left"]),
			(verticies["back"]["top-right"], verticies["front"]["top-right"]),
			(verticies["back"]["bottom-left"], verticies["front"]["bottom-left"]),
			(verticies["back"]["bottom-right"], verticies["front"]["bottom-right"]),
		]
		surfaces = [
			# Back face
			(
				verticies["back"]["top-left"],
				verticies["back"]["top-right"],
				verticies["back"]["bottom-right"],
				verticies["back"]["bottom-left"]
			),
			# Front face
			(
				verticies["front"]["top-left"],
				verticies["front"]["top-right"],
				verticies["front"]["bottom-right"],
				verticies["front"]["bottom-left"]
			),
			# Left Side
			(
				verticies["back"]["top-left"],
				verticies["back"]["bottom-left"],
				verticies["front"]["bottom-left"],
				verticies["front"]["top-left"]
			),
			# Right Side
			(
				verticies["back"]["top-right"],
				verticies["back"]["bottom-right"],
				verticies["front"]["bottom-right"],
				verticies["front"]["top-right"]
			),
			# Top Side
			(
				verticies["back"]["top-left"],
				verticies["back"]["top-right"],
				verticies["front"]["top-right"],
				verticies["front"]["top-left"]
			),
			# Bottom Side
			(
				verticies["back"]["bottom-left"],
				verticies["back"]["bottom-right"],
				verticies["front"]["bottom-right"],
				verticies["front"]["bottom-left"]
			),
		]
		self.shiftVal = Vector3D(0, 0, 0)
		return edges, surfaces

	def render(self):
		edges, surfaces = self.__getData()
		if not (self.rotated < 360):
			self.rotated = 0
		glPushMatrix()
		glRotated(self.rotated + self.rotateDegrees, self.rotateOn.x, self.rotateOn.y, self.rotateOn.z)
		self.rotated += self.rotateDegrees
		glBegin(GL_LINES)
		for edge in edges:
			for vertex in edge:
				glVertex3fv(vertex)
		glEnd()
		# glBegin(GL_QUADS)
		# for surface in surfaces:
		# 	for vertex in surface:
		# 		glColor3fv((0, 1, 0))
		# 		glVertex3fv(vertex)
		# glEnd()
		glPopMatrix()

	def move(self, vec):
		""" Permanent Translate. Doesn't reset at every frame. """
		self.origin.minus(vec, True)

	def shift(self, vec):
		""" Temporary Translate. Resets at every frame. """
		self.shiftVal.add(vec, True)