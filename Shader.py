import glm
import glfw
from OpenGL.GL import shaders
from OpenGL.GL import *


class Shader:

    def __init__(self, vertex_path, fragment_path):
        vertex_code = get_file_content(vertex_path)
        fragment_code = get_file_content(fragment_path)

        vertex = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex, vertex_code)
        glCompileShader(vertex)

        result = glGetShaderiv(vertex, GL_COMPILE_STATUS)
        if not (result):
            print("Vertex shader ERROR!")
            raise RuntimeError(glGetShaderInfoLog(vertex))

        fragment = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment, fragment_code)
        glCompileShader(fragment)

        result2 = glGetShaderiv(fragment, GL_COMPILE_STATUS)
        if not (result2):
            print("Fragment shader ERROR!")
            raise RuntimeError(glGetShaderInfoLog(vertex))

        self.ID = glCreateProgram()
        glAttachShader(self.ID, vertex)
        glAttachShader(self.ID, fragment)

        glLinkProgram(self.ID)

        success = glGetProgramiv(self.ID, GL_LINK_STATUS)
        if not success:
            print("gad darn")
            infolog = glGetProgramInfoLog(self.ID)
            print("ERROR::SHADER::PROGRAM::LINKING_FAILED\n", infolog)

        glDeleteShader(vertex)
        glDeleteShader(fragment)

    def set_mat4(self, name, matrix):
        glUniformMatrix4fv(glGetUniformLocation(self.ID, name), 1, GL_FALSE, glm.value_ptr(matrix))

    def use(self):
        glUseProgram(self.ID)

# Helper Function
def get_file_content(file):
    with open(file) as f:
        content = f.read()
    return content
