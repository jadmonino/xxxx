let distancia1 = 0
basic.forever(function () {
    MiniCar.led_rgb(LED_rgb_L_R.LED_L, LED_color.green1)
    MiniCar.led_show()
    MiniCar.LED_OFF()
    MiniCar.PWM_LED_L(pwm_led_l.pwm_red_r, 118)
    MiniCar.PWM_LED_R(pwm_led_r.pwm_green_l, 118)
    distancia1 = MiniCar.ultra()
    basic.showNumber(distancia1)
    basic.pause(100)
    if (distancia1 < 30) {
        MiniCar.motor(Motorlist.M1, Direction1.Forward, 0)
        MiniCar.motor(Motorlist.M2, Direction1.Forward, 0)
    } else {
        MiniCar.motor(Motorlist.M1, Direction1.Forward, 60)
        MiniCar.motor(Motorlist.M2, Direction1.Forward, 60)
    }
})
