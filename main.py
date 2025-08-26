basic.forever(function () {
    let left = Rover.LineTracking(Rover.TrackingState.L)
    let right = Rover.LineTracking(Rover.TrackingState.R)

    if (left == 0 && right == 0) {
        Rover.Move(100)
    }
    else if (left == 1 && right == 0) {
        Rover.MotorRunDual(-80, 80)
    }
    else if (left == 0 && right == 1) {
        Rover.MotorRunDual(80, -80)
    }
    else {
        Rover.Move(0)
    }
})