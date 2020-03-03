
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *
from components.Object3D.Box import Box

class Renderer3D:
	def __init__(self, size, fov, nearClip, farClip):
		self.size = size
		self.objects = {}
		self.fov = fov
		self.nearClip = nearClip
		self.farClip = farClip
		self.aspectRatio = size.x / size.y
		self.cameraPos = Vector3D(0, 0, 0)

	def updateSize(self, vec):
		self.size = vec
		glViewport(0, 0, vec.x, vec.y)
		self.setPerspective(self.fov, vec.x/vec.y, self.nearClip, self.farClip)
		self.moveCamera(Vector3D(0, 0, 5))

	# ===== Perspective =====

	def setPerspective(self, fov, ratio, nearClip, farClip):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(fov, ratio, nearClip, farClip)
		self.fov = fov
		self.aspectRatio = ratio
		self.nearClip = nearClip
		self.farClip = farClip

	# ===== Camera =====

	def moveCamera(self, vec):
		# glTranslatef(vec.x, vec.y, vec.z)
		self.cameraPos.add(vec, True)

	# ===== Objects =====

	def addObject(self, obj):
		self.objects[obj.name] = obj

	# ===== Render =====

	def render(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		# print(self.cameraPos.z)
		for objName, obj in self.objects.items():
			obj.shift(self.cameraPos.additive())
			obj.render()
		# self.objects["test_1"].render()
		# self.objects["test_2"].render()