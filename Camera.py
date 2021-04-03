import glm
import glfw
from OpenGL.GL import shaders
from OpenGL.GL import *
from ctypes import *
import numpy as np

class Camera:

    default_zoom = 0.05
    camera_face = 0

    def __init__(self):
        self.pos = glm.vec3(0.0, 0.0, 1.0)
        self.face = glm.vec3(0.0, 0.0, -1.0)
        self.up = glm.vec3(0.0, 1.0, 0.0)
        self.right = glm.normalize(glm.cross(self.up, glm.normalize(self.pos - self.face)))

    def get_view_mat(self):
        return glm.lookAt(self.cameraPos, self.cameraPos + self.cameraFace, self.cameraUp)

    def turn_left(self):
        self.camera_face = self.camera_face - glm.vec3(self.default_zoom, 0.0, 0.0)

    def turn_right(self):
        self.camera_face = self.camera_face + glm.vec3(self.default_zoom, 0.0, 0.0)
