import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dynamic_range = 3.3
dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_pins, GPIO.OUT)

def voltage_to_number(v):
    if not (0.0 <= v <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 -"
              f"{dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(v / dynamic_range * 255)

def dec2bin(n):
    return list(map(int, bin(n)[2:].zfill(8)))

def number_to_dac(n):
    if not (0 <= n <= 255):
        print("Число выходит за возможный диапазон [0, 255]")
        return
    bits = dec2bin(n)
    print(f"Число на вход ЦАП: {n}, биты: {bits}")
    GPIO.output(dac_pins, bits)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number_to_dac(voltage_to_number(voltage))
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    GPIO.output(dac_pins, 0)
    GPIO.cleanup()
