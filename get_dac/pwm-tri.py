import time
import pwm_dac as pwm
import signal_generator as sg

def triangle_wave(frequency, t):
    period = 1 / frequency
    x = (t % period) / period  # от 0 до 1

    if x < 0.5:
        return 2 * x           # 0 → 1
    else:
        return 2 * (1 - x)     # 1 → 0

amplitude = 1.5
offset = 1.65
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3, True)

    while True:
        voltage = offset + amplitude * triangle_wave(
            signal_frequency,
            time.monotonic()
        )
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
