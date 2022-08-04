function on_forever() {
    if (input.isGesture(Gesture.TiltLeft)) {
        dot.change(LedSpriteProperty.X, -1)
    } else if (input.isGesture(Gesture.TiltRight)) {
        dot.change(LedSpriteProperty.X, 1)
    } else if (input.isGesture(Gesture.LogoDown)) {
        dot.change(LedSpriteProperty.Y, -1)
    } else if (input.isGesture(Gesture.ScreenUp)) {
        dot.change(LedSpriteProperty.Y, 1)
    } else {
        
    }
    
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Abdul")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("---")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    `)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    images.createBigImage(`
        # . # . # . # . # .
                # . # . # . # . # .
                # . # . # . # . # .
                # . # . # . # . # .
                # . # . # . # . # .
    `).scrollImage(1, 200)
    images.createBigImage(`
        . . . . . . . . . .
                . . . . . . . . . .
                . . . . . . . . . .
                . . . . . . . . . .
                . . . . . . . . . .
    `).showImage(0)
})
function NewRound() {
    let timer = 0
    dot.set(LedSpriteProperty.X, randint(0, 4))
    if (timer == 0) {
        game.gameOver()
    }
    
}

let dot : game.LedSprite = null
let timernew = 0
dot = game.createSprite(2, 2)
game.startCountdown(50000)
