import RPi.GPIO as GPIO

def dec2bin(n):
    return list(map(int, bin(n)[2:].zfill(8)))

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.p = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

    def deinit(self):
        self.p.stop()
        GPIO.cleanup()

    def set_voltage(self, voltage):
        self.p.start(voltage / self.dynamic_range * 100)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
   
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()
