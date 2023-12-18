import pyglet

# few options
pyglet.options["shadow_window"] = False
pyglet.options['debug_gl'] = False

import pyglet.gl as gl

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window, self).__init__(**args)

    def on_draw(self):
        gl.glClearColor(2.0, 0.5, 1.0, 1.0)
        self.clear()

    def on_resize(self, width, height):
        print(f'resize {width} * {height}' )

class Game:
    def __init__(self):
        self.config = gl.Config(major_version = 3)
        self.window = Window(config = self.config, width = 800, height = 600, caption = 'Mincraft_clone', resizable = True, vsync = False)

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    game = Game()
    game.run()
    