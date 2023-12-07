from settings import *
from world import World

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)

    def update(self):
        pass

    def render(self):
        self.world.render()











































