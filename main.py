from ursina import *

app = Ursina()

cube = Entity(model='cube',color=color.orange, scale=(2,2,2), texture='white_cube')

def update():
    cube.rotation_y += 1
    cube.rotation_x += 0.5

def input(key):
    if key == 'space':
        cube.color = color.random_color()

app.run()