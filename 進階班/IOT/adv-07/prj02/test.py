import mcu

gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, True)
# LED.R.value(0)
# LED.B.value(0)
# LED.G.value(0)
LED.R.duty(1023)
LED.B.duty(1023)
LED.G.duty(1023)
