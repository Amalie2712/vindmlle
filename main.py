from microbit import *
import utime

# Constants for the voltage divider (adjust according to your setup)
R1 = 10000  # Resistor in ohms
R2 = 10000  # Resistor in ohms

def read_voltage():
    try:
        # Read analog value from pin0 (adjust according to your setup)
        analog_value = pin0.read_analog()
        
        # Convert analog value to voltage (0-3.3V)
        voltage = (analog_value / 1023.0) * 3.3
        
        # Calculate actual voltage considering the voltage divider
        actual_voltage = voltage * (R1 + R2) / R2
        
        return actual_voltage
    except Exception as e:
        display.scroll(str(e))
        return None

def log_voltage(log_file, voltage, timestamp):
    # Log voltage with timestamp
    log_entry = '{}: {:.2f}V\n'.format(timestamp, voltage)
    log_file.write(log_entry)

# Open a file for logging
with open('voltage_log.txt', 'w') as log_file:
    while True:
        # Read voltage
        voltage = read_voltage()
        
        if voltage is not None:
            # Get current time in milliseconds since micro:bit was turned on
            timestamp = utime.ticks_ms()
            
            # Log voltage
            log_voltage(log_file, voltage, timestamp)
        
        # Wait a bit before the next measurement
        sleep(1000)


