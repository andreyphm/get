import r2r_dac as r2r
import signal_generator as sg
import time

def triangle_wave(frequency, t):
    period = 1 / frequency
    x = (t % period) / period  # от 0 до 1

    if x < 0.5:
        return 2 * x           # 0 → 1
    else:
        return 2 * (1 - x)     # 1 → 0

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
    while True:
        value = amplitude * triangle_wave(signal_frequency, time.monotonic())
        dac.set_voltage(value)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
