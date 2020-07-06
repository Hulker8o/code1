input.onButtonPressed(Button.A, function () {
    basic.showString("Yes")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("No")
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Maybe")
})
basic.showString("Ask")
