import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [x, y, dx, y, dx, dy, x, dy]))

pyglet.app.run()