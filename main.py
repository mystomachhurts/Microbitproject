def on_forever():
    if input.is_gesture(Gesture.TILT_LEFT):
        dot.change(LedSpriteProperty.X, -1)
    elif input.is_gesture(Gesture.TILT_RIGHT):
        dot.change(LedSpriteProperty.X, 1)
    elif input.is_gesture(Gesture.LOGO_DOWN):
        dot.change(LedSpriteProperty.Y, -1)
    elif input.is_gesture(Gesture.SCREEN_UP):
        dot.change(LedSpriteProperty.Y, 1)
    else:
        pass

def on_button_pressed_a():
    basic.show_string("Abdul")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("---")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    images.create_big_image("""
        # . # . # . # . # .
                # . # . # . # . # .
                # . # . # . # . # .
                # . # . # . # . # .
                # . # . # . # . # .
    """).scroll_image(1, 200)
    images.create_big_image("""
        . . . . . . . . . .
                . . . . . . . . . .
                . . . . . . . . . .
                . . . . . . . . . .
                . . . . . . . . . .
    """).show_image(0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def NewRound():
    timer = 0
    dot.set(LedSpriteProperty.X, randint(0, 4))
    if timer == 0:
        game.game_over()
dot: game.LedSprite = None
timernew = 0
dot = game.create_sprite(2, 2)
game.start_countdown(50000)