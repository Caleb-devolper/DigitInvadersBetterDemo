def on_button_pressed_a():
    PLAYER.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global SHOOT
    SHOOT = game.create_sprite(PLAYER.get(LedSpriteProperty.X),
        PLAYER.get(LedSpriteProperty.Y))
    SHOOT.set(LedSpriteProperty.BRIGHTNESS, 105)
    for index in range(4):
        SHOOT.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if SHOOT.get(LedSpriteProperty.Y) <= 0:
            SHOOT.delete()
        if SHOOT.is_touching(ENEMY):
            game.add_score(1)
        if SHOOT.is_touching(ENEMY):
            SHOOT.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    PLAYER.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

SHOOTENEMY: game.LedSprite = None
SHOOT: game.LedSprite = None
ENEMY: game.LedSprite = None
PLAYER: game.LedSprite = None
basic.show_string("3 2 1 BATTLE")
basic.show_icon(IconNames.TORTOISE)
game.set_score(0)
game.set_life(5)
PLAYER = game.create_sprite(2, 4)
ENEMY = game.create_sprite(0, 0)

def on_forever():
    global SHOOTENEMY
    ENEMY.move(1)
    basic.pause(100)
    ENEMY.if_on_edge_bounce()
    SHOOTENEMY = game.create_sprite(ENEMY.get(LedSpriteProperty.X),
        ENEMY.get(LedSpriteProperty.Y))
    SHOOTENEMY.set(LedSpriteProperty.BRIGHTNESS, 100)
    for index2 in range(4):
        SHOOTENEMY.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
        if SHOOTENEMY.is_touching(PLAYER):
            game.remove_life(1)
        if SHOOTENEMY.get(LedSpriteProperty.Y) >= 4:
            SHOOTENEMY.delete()
basic.forever(on_forever)
