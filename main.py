distancia1 = 0

def on_forever():
    # global distancia1
    MiniCar.led_rgb(LED_rgb_L_R.LED_L, LED_color.GREEN1)
    MiniCar.led_show()
    MiniCar.LED_OFF()
    MiniCar.PWM_LED_L(pwm_led_l.PWM_RED_R, 118)
    MiniCar.PWM_LED_R(pwm_led_r.PWM_GREEN_L, 118)
    distancia1 = MiniCar.ultra()
    basic.show_number(distancia1)
    basic.pause(100)
    if distancia1 < 30:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 0)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 0)
    else:
        MiniCar.motor(Motorlist.M1, Direction1.FORWARD, 60)
        MiniCar.motor(Motorlist.M2, Direction1.FORWARD, 60)
basic.forever(on_forever)
