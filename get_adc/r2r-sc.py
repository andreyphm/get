from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist
import time

try:
    max_voltage = 3.3
    adc = R2R_ADC(max_voltage)
    voltage_values = []
    time_values = []
    duration = 3.0
    start = time.monotonic()
    now = start
    while now - start < duration:
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(now - start)
        now = time.monotonic()
    plot_voltage_vs_time(time_values, voltage_values, max_voltage)
    plot_sampling_period_hist(time_values)
finally:
    adc.deinit()
