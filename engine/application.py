
"""
	Contains the `Application` class.
	`Application` class is the top-most level class which controls/manifest all components.
	It is built around pygame and is the only way to interact with the engine.
"""

# Imports
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from renderer3D import Renderer3D
from utils import *

# ===============================================================================================

# Main Code

class Application:

	# Init class
	def __init__(self, title, size=Vector2D(1000, 600)):
		""" Defines all the required initial things. """
		self.title = title
		self.size = size
		self.renderer3D = Renderer3D(self.size, 60, 0.1, 50.0)

	# Update Size
	def updateSize(self, width, height):
		""" Event triggered when the application window is resized. """
		self.size = Vector2D(width, height)

		# Trigger the resize event in the renderers
		self.renderer3D.updateSize(Vector2D(width, height))

	# Run
	def run(self):
		""" The run loop """
		# Initialise pygame
		pygame.init()
		pygame.display.set_caption(self.title)
		pygame.display.set_mode(self.size.toTuple(), DOUBLEBUF|OPENGL|RESIZABLE)

		# # Renderer settings (Can be done here)
		# self.renderer3D.setPerspective(60, self.size[0]/self.size[1], 0.1, 50.0)
		# # Not required because it happens automatically in self.renderer3D.updateSize()
		# self.renderer3D.moveCamera(Vector3D(0, 0, -5))

		# Loop
		while True:

			# Listen for events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					# Quit Event
					pygame.quit()
					quit()
				elif event.type == pygame.VIDEORESIZE:
					# Window resize event
					self.updateSize(event.w, event.h)
			
			# Render the scene
			self.renderer3D.render()

			# Update the display and wait
			pygame.display.flip()
			pygame.time.wait(10)