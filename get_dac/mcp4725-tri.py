from mcp4725_driver import MCP4725
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
    mcp4725 = MCP4725(5.11, 0x61, True)
    while True:
        mcp4725.set_voltage(amplitude *
            triangle_wave(signal_frequency, time.monotonic()))
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    mcp4725.deinit()
