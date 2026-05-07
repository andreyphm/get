import RPi.GPIO as GPIO
import time

COMPARATOR_WAIT_TIME = 0.01

def dec2bin(n):
    return [int(c) for c in bin(n)[2:].zfill(8)]

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        if not (0 <= number <= 255):
            print("Число выходит за возможный диапазон [0, 255]")
            return
        GPIO.output(self.bits_gpio, dec2bin(number))

    def sequential_counting_adc(self):
        for value in range(256):
            self.number_to_dac(value)
            time.sleep(COMPARATOR_WAIT_TIME)
            res = GPIO.input(self.comp_gpio)
            if res:
                return value
        return 255

    def get_sc_voltage(self):
        return self.sequential_counting_adc() / 255 * self.dynamic_range

    def successive_approximation_adc(self):
        res = 0
        for i in range(7, -1, -1):
            w = 1 << i
            self.number_to_dac(res + w)
            time.sleep(COMPARATOR_WAIT_TIME)
            greater = GPIO.input(self.comp_gpio)
            if not greater:
                res += w
        return res

    def get_sar_voltage(self):
        return self.successive_approximation_adc() / 255 * self.dynamic_range
        

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3)
        while True:
            print(f"Полученное напряжение: {adc.get_sar_voltage():.2f}")
    finally:
        adc.deinit()
