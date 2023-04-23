input.onButtonPressed(Button.A, function () {
    PLAYER.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    SHOOT = game.createSprite(PLAYER.get(LedSpriteProperty.X), PLAYER.get(LedSpriteProperty.Y))
    SHOOT.set(LedSpriteProperty.Brightness, 105)
    for (let index = 0; index < 4; index++) {
        SHOOT.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if (SHOOT.get(LedSpriteProperty.Y) <= 0) {
            SHOOT.delete()
        }
        if (SHOOT.isTouching(ENEMY)) {
            game.addScore(1)
        }
        if (SHOOT.isTouching(ENEMY)) {
            SHOOT.delete()
        }
    }
})
input.onButtonPressed(Button.B, function () {
    PLAYER.change(LedSpriteProperty.X, 1)
})
let SHOOTENEMY: game.LedSprite = null
let SHOOT: game.LedSprite = null
let ENEMY: game.LedSprite = null
let PLAYER: game.LedSprite = null
basic.showString("3 2 1 BATTLE")
basic.showIcon(IconNames.Tortoise)
game.setScore(0)
game.setLife(5)
PLAYER = game.createSprite(2, 4)
ENEMY = game.createSprite(0, 0)
basic.forever(function () {
    ENEMY.move(1)
    basic.pause(100)
    ENEMY.ifOnEdgeBounce()
    SHOOTENEMY = game.createSprite(ENEMY.get(LedSpriteProperty.X), ENEMY.get(LedSpriteProperty.Y))
    SHOOTENEMY.set(LedSpriteProperty.Brightness, 100)
    for (let index = 0; index < 4; index++) {
        SHOOTENEMY.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
        if (SHOOTENEMY.isTouching(PLAYER)) {
            game.removeLife(1)
        }
        if (SHOOTENEMY.get(LedSpriteProperty.Y) >= 4) {
            SHOOTENEMY.delete()
        }
    }
})
