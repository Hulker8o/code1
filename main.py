def on_button_pressed_a():
    basic.show_string("Yes")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("No")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("Maybe")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("Ask a question")