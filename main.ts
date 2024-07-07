bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
    servo_control()
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
function servo_control () {
    for (let index = 0; index < 3; index++) {
        // Loop to perform the actions 3 times
        pins.digitalWritePin(DigitalPin.P8, 0)
        basic.pause(50)
        // Pause time reduced for faster operation
        pins.digitalWritePin(DigitalPin.P8, 1)
        for (let index = 0; index < 6; index++) {
            // Increased the loop count
            pins.digitalWritePin(DigitalPin.P14, 0)
            basic.pause(100)
            // Pause time reduced for faster operation
            pins.digitalWritePin(DigitalPin.P14, 1)
            basic.pause(100)
        }
        // Pause time reduced for faster operation
        pins.servoWritePin(AnalogPin.P16, 120)
        basic.pause(150)
        // Pause time reduced for faster operation
        pins.servoWritePin(AnalogPin.P16, 67)
        basic.pause(150)
        // Pause time reduced for faster operation
        code = 40
        for (let index = 0; index < 20; index++) {
            // Increased the loop count
            code += 1
            pins.servoWritePin(AnalogPin.P16, code)
            basic.pause(12)
        }
        // Pause time reduced for faster operation
        pins.servoWritePin(AnalogPin.P16, 90)
        pins.digitalWritePin(DigitalPin.P14, 0)
        basic.pause(250)
    }
}
let code = 0
bluetooth.startUartService()
bluetooth.startLEDService()
basic.showIcon(IconNames.Heart)
