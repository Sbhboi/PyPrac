from ursina import *

app = Ursina()

player = Entity(model='cube',color=color.azure, scale=(1,2,1), collider='box', y=1)

ground = Entity(model='plane', scale=32, texture='white_cube', texture_scale=(32,32), color=color.lime)

def update():
    player.x +=held_keys['d'] * time.dt * 5
    player.x -=held_keys['a'] * time.dt * 5
    player.y +=held_keys['w'] * time.dt * 5
    player.y -=held_keys['s'] * time.dt * 5

    if held_keys['q']:
        application.quit()
        
EditorCamera()

app.run()