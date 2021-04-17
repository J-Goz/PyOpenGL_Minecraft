import glm
import glfw
from OpenGL.GL import shaders
from OpenGL.GL import *
from ctypes import *
import numpy as np

class Camera:

    default_zoom = 0.05
    camera_face = 0

    def __init__(self, shader, SCR_WIDTH, SCR_HEIGHT):
        self.pos = glm.vec3(0.0, 0.1, 1.0)
        self.face = glm.vec3(0.0, 0.0, -1.0)
        self.up = glm.vec3(0.0, 1.0, 0.0)
        self.right = glm.normalize(glm.cross(self.up, glm.normalize(self.pos - self.face)))

        self.view = self.get_view_mat()
        self.projection = glm.perspective(glm.radians(45.0), (SCR_WIDTH / SCR_HEIGHT), 0.1, 100.0)
        self.shader = shader

    def update(self):
        self.shader.use()
        self.shader.set_mat4("view", self.view)
        self.shader.set_mat4("projection", self.projection)

    def get_view_mat(self):
        return glm.lookAt(self.pos, self.pos + self.face, self.up)

    def turn_left(self):
        self.camera_face = self.camera_face - glm.vec3(self.default_zoom, 0.0, 0.0)

    def turn_right(self):
        self.camera_face = self.camera_face + glm.vec3(self.default_zoom, 0.0, 0.0)
