import glm
import glfw
from OpenGL.GL import shaders
from OpenGL.GL import *
from ctypes import *
import numpy as np
import Shader


class Grid:
    vertexArray = []
    indexArray = []
    model = glm.mat4(1)
    shader = None

    def __init__(self):
        self.create_vertex_array()
        self.create_index_array()

        self.vao = GLuint()
        self.vbo = GLuint()
        self.ebo = GLuint()

        self.vertexArray = np.array(self.vertexArray, dtype=np.float32)
        self.indexArray = np.array(self.indexArray, dtype=np.float32)

        # Bind vao
        glGenVertexArrays(1, self.vao)
        glBindVertexArray(self.vao)

        # Upload Vertex Buffer (VBO) to the GPU, keep a reference to it (vertexBufferObject)
        glGenBuffers(1, self.vbo)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertexArray.nbytes, self.vertexArray, GL_STATIC_DRAW)

        # Upload Index Buffer (EBO) to the GPU, keep a reference to it (elementBufferObject)
        glGenBuffers(1, self.ebo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indexArray.nbytes, self.indexArray, GL_STATIC_DRAW)

        # Position
        glVertexAttribPointer(0,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              24,
                              ctypes.c_void_p(0)
                              )
        glEnableVertexAttribArray(0)

        # Color
        glVertexAttribPointer(1,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              24,
                              ctypes.c_void_p(12)
                              )
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

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

