
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *
from components.Object3D.Box import Box
from components.Plotter import Plotter

class Renderer3D:
	def __init__(self, size, fov, nearClip, farClip):
		self.size = size
		self.objects = {}
		self.fov = fov
		self.nearClip = nearClip
		self.farClip = farClip
		self.aspectRatio = size.x / size.y
		self.camera = Camera3D()
		self.plotter = Plotter(self.size)

	def updateSize(self, vec):
		self.size = vec
		self.plotter.updateSize(vec)
		glViewport(0, 0, vec.x, vec.y)
		self.setPerspective(self.fov, vec.x/vec.y, self.nearClip, self.farClip)

	# ===== Perspective =====

	def setPerspective(self, fov, ratio, nearClip, farClip):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(fov, ratio, nearClip, farClip)
		self.fov = fov
		self.aspectRatio = ratio
		self.nearClip = nearClip
		self.farClip = farClip

	# ===== Objects =====

	def addObject(self, obj):
		self.objects[obj.name] = obj

	# ===== Render =====

	def render(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		for objName, obj in self.objects.items():
			obj.shift(self.camera.pos.additive())
			obj.render(self.plotter)
		# self.plotter.line(Vector3D(-1, 0, -1), Vector3D(1, 0, -1))

# ================================================================================================

class Camera3D:

	# Init
	def __init__(self):
		self.pos = Vector3D(0, 0, 0)

	# Set Camera Position as per user
	def setCamPos(self, pos):
		self.pos = pos

	# Move
	def move(self, vec):
		""" Changes the viewpoint of the whole scene """
		# Z-axis Values work the opposite
		self.pos.add(vec, autoSet=True)