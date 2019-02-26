import csv
import scipy.integrate as it
import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs = 19.23 # Sampling frequency


dx_times = []

### open csv file and get required parameters ###
def get_csv_data():
	timestamps = []
	z_accels= []
	with open('test3/datalog.csv', 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			if row:
				#print row
				timestamps.append (row[-1])
				z_accels.append(float(row[2]))


	return [timestamps,z_accels]


### convert the millisecond timestamps into a suitable time x axis ###

def format_millis_to_xaxis(timestamps):
	array_length = len(timestamps)
	dx_times.append(0.00)
	for idx in range(array_length-1):
		dx_times.append( (float(timestamps[idx+1]) - float(timestamps[0]))/1000)
	
	return dx_times
	
x_axis = copy.copy(dx_times)

### filter the acceleration data ###
def filter_accel_data(z_accels):
	fc = 2  # Cut-off frequency of the filter
	w = float(fc / (fs / 2)) # Normalize the frequency
	b, a = signal.butter(5, w, 'low')
	filtered_z_axis = signal.filtfilt(b, a, z_accels)
	return filtered_z_axis
	
	
### integrate the z axis data twice to get displacement ###	
def double_integrate_data(z_accels, dx_times):
	velocity = it.cumtrapz(filtered_z_axis,dx_times)

	print len(velocity)
	detrended_velocity = signal.detrend(velocity)
	location = it.cumtrapz(velocity,dx_times[:-1])
	return [velocity,location]



### double integrate the acceleration data in chunks ###
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]
        
#velocity_chunk = []
#location_chunk = []
#for h in range(len(dx_times)):
#	velocity_chunk = it.cumtrapz(filtered_z_axis,dx_times)
#	location_chunk = it.cumtrapz(velocity,dx_times)


### plot the data ###

def plot_data(z_accels, filtered_z_axis, velocity, location, dx_times):
	plt.plot(dx_times, z_accels, label='z-axis acceleration')
	plt.plot(dx_times, filtered_z_axis, label='filtered z-axis acceleration')

	plt.plot(dx_times[:-1], velocity, label='z-axis velocity')
	plt.plot(dx_times[:-2], location, label='location')
	plt.ylabel('Acceleration ($ms^{2}$)')
	plt.xlabel('Time (Seconds)')
	plt.legend()
	plt.show()


#for i in range(len(location)):
#	print str("%.2f" % z_accels[i]) + "," + str("%.2f" % velocity[i]) + "," + str("%.2f" % location[i])


timestamps, z_accels = get_csv_data()
dx_times = format_millis_to_xaxis(timestamps)
filtered_z_axis = filter_accel_data(z_accels)
velocity, location = double_integrate_data(filtered_z_axis, dx_times)
plot_data(z_accels, filtered_z_axis, velocity, location, dx_times)
