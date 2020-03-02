
class Vector3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	# ===== Conversions =====
	
	def toTuple(self):
		return (self.x, self.y, self.z)

	def __str__(self):
		return "{}".format(self.toTuple())

	# ===== Operations =====

	def add(self, vec, autoSet=False):
		if autoSet:
			self.x += vec.x
			self.y += vec.y
			self.z += vec.z
		elif not autoSet:
			return Vector3D(self.x + vec.x, self.y + vec.y, self.z + vec.z)
		else:
			return None
	
	def minus(self, vec, autoSet=False):
		if autoSet:
			self.x -= vec.x
			self.y -= vec.y
			self.z -= vec.z
		elif not autoSet:
			return Vector3D(self.x - vec.x, self.y - vec.y, self.z - vec.z)
		else:
			return None

	def multiply(self, vec, autoSet=False):
		if autoSet:
			self.x *= vec.x
			self.y *= vec.y
			self.z *= vec.z
		elif not autoSet:
			return Vector3D(self.x * vec.x, self.y * vec.y, self.z * vec.z)
		else:
			return None

	def divide(self, vec, autoSet=False):
		if autoSet:
			self.x /= vec.x
			self.y /= vec.y
			self.z /= vec.z
		elif not autoSet:
			return Vector3D(self.x / vec.x, self.y / vec.y, self.z / vec.z)
		else:
			return None

	def additive(self, autoSet=False):
		if autoSet:
			self.x = -(self.x)
			self.y = -(self.y)
			self.z = -(self.z)
		elif not autoSet:
			return Vector3D(-(self.x), -(self.y), -(self.z))
		else:
			None