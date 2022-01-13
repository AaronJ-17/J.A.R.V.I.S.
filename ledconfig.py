from gpiozero import LED
led_up = LED(2)
led_down_up = LED(18)

#center leds on
def led_on():
    led_up.on()

#center leds off
def led_off():
    led_up.off()
    
#side leds on
def led_side_on():
    led_down_up.on()
    
#side leds off
def led_side_off():
    led_down_up.off()

#both leds on
def both_leds_on():
    led_up.on()
    led_down_up.on()

#both leds off
def both_leds_off():
    led_up.off()
    led_down_up.off()
