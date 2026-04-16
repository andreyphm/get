import time
import pwm_dac as pwm
import signal_generator as sg

amplitude = 1.5
offset = 1.65
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3, True)

    while True:
        voltage = offset + amplitude * sg.get_sin_wave_amplitude(
            signal_frequency,
            time.monotonic()
        )
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
