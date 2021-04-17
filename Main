import glfw
import glm
import numpy as np
from OpenGL.GL import *
import Shader
import Grid
import Camera

# Settings
SCR_WIDTH = 800
SCR_HEIGHT = 600


def get_file_content(file):
    with open(file) as f:
        content = f.read()
    return content


def framebuffer_size_callback(window, width, height):
    if width != 0 and height != 0:
        width = width
        height = height
        glViewport(0, 0, width, height)


def main():
    # Initialize the library
    glfw.glewExperimental = GL_TRUE

    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(SCR_WIDTH, SCR_HEIGHT, "OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    shader = Shader.Shader("VertexShader.vsh", "FragmentShader.fsh")

    camera = Camera.Camera(shader, SCR_WIDTH, SCR_HEIGHT)
    grid = Grid.Grid()
    glUseProgram(shader.ID)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shader.ID)

        camera.update()
        grid.draw(shader)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
