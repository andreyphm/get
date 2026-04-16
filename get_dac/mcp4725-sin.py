from mcp4725_driver import MCP4725
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp4725 = MCP4725(5.11, 0x61, True)
    while True:
        mcp4725.set_voltage(amplitude *
            sg.get_sin_wave_amplitude(signal_frequency, time.monotonic()))
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    mcp4725.deinit()
