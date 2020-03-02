
from application import Application
from components.Object3D.Box import Box
from utils import *

app = Application("Test...", size=(1000, 600))
app.renderer3D.addObject(Box("test_1", Vector3D(0, 0, 0), Vector3D(2, 2, 2)))
# app.renderer3D.addObject(Box("test_2", Vector3D(-1, 0, 0), Vector3D(2, 2, 2)))
# app.renderer3D.objects["test_1"].rotate(1, Vector3D(3, 1, 1))
app.run()