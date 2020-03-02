
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from renderers import Renderer3D
from utils import *
from components.Object3D.Box import Box

class Application:
	def __init__(self, title, size=(800, 600)):
		self.title = title
		self.size = size
		self.renderer3D = Renderer3D(self.size)

	def updateSize(self, width, height):
		self.size = (width, height)
		self.renderer3D.updateSize(width, height)

	def run(self):
		pygame.init()
		pygame.display.set_caption(self.title)
		pygame.display.set_mode(self.size, DOUBLEBUF|OPENGL|RESIZABLE)
		self.renderer3D.setPerspective(60, self.size[0]/self.size[1], 0.1, 50.0)
		# # Not required because it happens automatically in self.renderer3D.updateSize()
		# self.renderer3D.moveCamera(Vector3D(0, 0, -5))
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.VIDEORESIZE:
					self.updateSize(event.w, event.h)
			self.renderer3D.render()
			pygame.display.flip()
			pygame.time.wait(10)

app = Application("Test...", size=(1000, 600))
app.renderer3D.addObject(Box("test_1", Vector3D(0, 0, 0), Vector3D(2, 2, 2)))
# app.renderer3D.addObject(Box("test_2", Vector3D(-1, 0, 0), Vector3D(2, 2, 2)))
# app.renderer3D.objects["test_1"].rotate(1, Vector3D(3, 1, 1))
app.run()