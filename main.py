from ursina import *

app = Ursina()

player = Entity(
    model='cube',
    color=color.azure, 
    scale=(1,1,1), 
    y=0,
    z=0
)

ground = Entity(
    model='plane', 
    scale=32, 
    texture='white_cube', 
    texture_scale=(32,32), 
    color=color.lime,
    rotation_x=90,
    y=-0.5,
    z=1
)

food = Entity(
    model='sphere',
    color=color.red,
    scale=0.5,
    position=(3,3,0)
)

def update():
    player.x +=held_keys['d'] * time.dt * 5
    player.x -=held_keys['a'] * time.dt * 5
    player.y +=held_keys['w'] * time.dt * 5
    player.y -=held_keys['s'] * time.dt * 5

    if distance_2d(player, food) < 0.7:
        import random
        food.x = random.uniform(-4,4)
        food.y = random.uniform(-4,4)

        player.scale += 0.5
        print("Yummeh !")

    if held_keys['q']:
        application.quit()
            
camera.orthographic = True
camera.fov = 10

app.run()