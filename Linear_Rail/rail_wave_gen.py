import serial
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# User-defined parameters
frequency = 0.2      # Frequency of the sine wave in Hz
amplitude = 1.0      # Amplitude of the sine wave
num_cycles = 5       # Number of cycles to generate
serial_port = 'COM7'  # Adjust the port to your system
baud_rate = 9600     # Adjust the baud rate as needed

# Calculate the number of data points for the given parameters
sampling_frequency = 100  # Adjust as needed (higher for smoother visualization)
num_samples = int(sampling_frequency * num_cycles)
time = np.linspace(0, num_cycles / frequency, num_samples)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

# Initialize the serial port
ser = serial.Serial(serial_port, baud_rate)

# Create a figure and plot the sine wave
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(time, sine_wave, label='Sine Wave')
red_line, = ax.plot([time[0], time[0]], [-1.2 * amplitude, 1.2 * amplitude], 'r', linewidth=2, label='Red Line')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Real-time Sine Wave Transmission')
ax.legend()

# Send sine wave data over the serial port in real-time
for i in range(num_samples):
    ser.write(f'{sine_wave[i]}\n'.encode('utf-8'))
    
    # Update the red line's position
    red_line.set_xdata([time[i], time[i]])
    plt.pause(0.01)

# Close the serial port when done
ser.close()

# Keep the plot window open until manually closed
plt.ioff()
plt.show()
