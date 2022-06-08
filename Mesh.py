import glm
import glfw
from OpenGL.GL import shaders
from OpenGL.GL import *
from ctypes import *
import numpy as np
import Shader


class Mesh:

    vertexArray = []
    indexArray = []

    shader = None

    def __init__(self):
        self.vao = GLuint()
        self.vbo = GLuint()
        self.ebo = GLuint()

        self.model = glm.mat4(1)

        self.create_vertex_array()
        self.create_index_array()

        self.vertexArray = np.array(self.vertexArray, dtype=np.float32)
        self.indexArray = np.array(self.indexArray, dtype=np.uint32)

        # Generate & Bind vao
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










