import glm
import glfw
from OpenGL.GL import shaders
from OpenGL.GL import *
from ctypes import *
import numpy as np
import Shader
from Mesh import Mesh


class Grid(Mesh):
    vertexArray = []
    indexArray = []

    shader = None


    def __init__(self):
        super().__init__()

    def create_vertex_array(self):
        # DATA stored in VAO
        for x in range(-100, 100, 2):
            # To draw lines across x axis from z = -1 to z = 1
            self.vertexArray.append(glm.vec3(x / 100, 0.0, -1.0))  # Vertex position 1
            self.vertexArray.append(glm.vec3(1.0, 1.0, 1.0))  # color for v1
            self.vertexArray.append(glm.vec3(x / 100, 0.0, 1.0))  # Vertex position 2
            self.vertexArray.append(glm.vec3(1.0, 1.0, 1.0))  # color for v2

        for z in range(-100, 100, 2):
            # To draw lines across z axis from x = -1 to x = 1
            self.vertexArray.append(glm.vec3(-1.0, 0.0, z / 100))  # Vertex position 1
            self.vertexArray.append(glm.vec3(1.0, 1.0, 1.0))  # color for v1
            self.vertexArray.append(glm.vec3(1.0, 0.0, z / 100))  # Vertex position 2
            self.vertexArray.append(glm.vec3(1.0, 1.0, 1.0))  # color for v2

    def create_index_array(self):
        for i in range(20000):
            self.indexArray.append(i)

    def draw(self, shader):
        self.shader = shader
        self.shader.use()
        glBindVertexArray(self.vao)
        self.shader.set_mat4("model", self.model)
        glDrawElements(GL_LINES, 20000, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)