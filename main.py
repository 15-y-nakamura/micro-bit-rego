def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
    servo_control()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def servo_control():
    global code
    for _ in range(3):  # Loop to perform the actions 3 times
        pins.digital_write_pin(DigitalPin.P8, 0)
        basic.pause(50)  # Pause time reduced for faster operation
        pins.digital_write_pin(DigitalPin.P8, 1)
        for index in range(6):  # Increased the loop count
            pins.digital_write_pin(DigitalPin.P14, 0)
            basic.pause(100)  # Pause time reduced for faster operation
            pins.digital_write_pin(DigitalPin.P14, 1)
            basic.pause(100)  # Pause time reduced for faster operation
        pins.servo_write_pin(AnalogPin.P16, 120)
        basic.pause(150)  # Pause time reduced for faster operation
        pins.servo_write_pin(AnalogPin.P16, 67)
        basic.pause(150)  # Pause time reduced for faster operation
        code = 40
        for index2 in range(20):  # Increased the loop count
            code += 1
            pins.servo_write_pin(AnalogPin.P16, code)
            basic.pause(12)  # Pause time reduced for faster operation
        pins.servo_write_pin(AnalogPin.P16, 90)
        pins.digital_write_pin(DigitalPin.P14, 0)
        basic.pause(250)  # Pause time reduced for faster operation

code = 0
bluetooth.start_uart_service()
bluetooth.start_led_service()
basic.show_icon(IconNames.HEART)