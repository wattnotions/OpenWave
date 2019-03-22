import csv
import scipy.integrate as it
import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sys
fs = 19.23 # Sampling frequency





### open csv file and get required parameters ###
###csv format : (lin accel) X, Y, Z, (Euler) X, Y, Z, (MAG) X, Y , TIMESTAMP######


def get_csv_data():
	timestamps = []
	z_accels   = []
	pitch      = []
	roll       = []
	with open('test_data/datalog.csv', 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			if row:
				#print row
				timestamps.append (row[-1])
				z_accels.append(float(row[2]))
				pitch.append(float(row[3]))
				roll.append(float(row[4]))
				


	return [timestamps,z_accels, pitch, roll]


### convert the millisecond timestamps into a suitable time x axis ###

def format_millis_to_xaxis(timestamps, scale_factor):
	dx_times = []

	array_length = len(timestamps)
	dx_times.append(0.00)
	for idx in range(array_length-1):
		dx_time = ( (float(timestamps[idx+1]) - float(timestamps[0]))/scale_factor)##make scale factor 1000 to go from secods to milliseconds
		dx_time = round(dx_time, 8)
		dx_times.append(dx_time)
	
	return dx_times
	
### filter the acceleration data ###
def filter_accel_data(z_accels):
	fc = 2  # Cut-off frequency of the filter
	w = float(fc / (fs / 2)) # Normalize the frequency
	b, a = signal.butter(5, w, 'low')
	filtered_z_axis = signal.filtfilt(b, a, z_accels)
	return filtered_z_axis
	
	
### integrate the z axis data twice to get displacement ###	
def double_integrate_data(z_accels, dx_times):
	velocity = it.cumtrapz(z_accels,dx_times)

	detrended_velocity = signal.detrend(velocity)
	location = it.cumtrapz(velocity,dx_times[:-1])
	return [velocity,location]



### split a list into chunks of size n ###
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


### integrate the acceleration data in chunks ###
def chunk_integrate(dx_times, filtered_z_axis, peaks):        
	z_accels_chunks = []
	x_axis_chunks   = []
	zeroed_x_axis   = []
	velocity_chunk  = []
	location_chunk  = []

	#for x in chunks(filtered_z_axis, 77):
	#	z_accels_chunks.append(x)
		
	#for y in chunks(dx_times, 77):
	#	x_axis_chunks.append(y)
	
	len_array = len(peaks)
	
	for idx in range(len_array-1):
		z_accels_chunks.append(filtered_z_axis[peaks[idx]:peaks[idx+1]])
		x_axis_chunks.append(dx_times[peaks[idx]:peaks[idx+1]])
		
	
	for i in x_axis_chunks[:10]:
		zeroed_x_axis.append((format_millis_to_xaxis(i,1)))


	for idx, h in enumerate(x_axis_chunks):
		velocity_chunk.append(it.cumtrapz(z_accels_chunks[idx],h))
		location_chunk.append(it.cumtrapz(velocity_chunk[-1],h[:-1]))
	
	stitched_location = []
	max_heights       = []
	
	
	
	#check each chunk for the max displacement in that chunk
	for h in location_chunk:
		max_heights.append(float(max(h)))
		print (max(h))
	
	avg_max_displacement =  (sum(max_heights) / float(len(max_heights)))

	#stitch all of the chunks together	
	for x in location_chunk:
		for y in x:
			stitched_location.append(y)
			
	#get the average displacement of the data and remove any offset present
	displacement_offset =  sum(stitched_location) / float(len(stitched_location))
	stitched_location_offset_adj = []	
	for h in stitched_location:
		stitched_location_offset_adj.append(h - float(displacement_offset))
		
		
		
	print len(stitched_location)
	print len(dx_times)
	
	print "Displacement Offset = " + str(displacement_offset) + " Meters"		
	print "Average Maximum Displacement = " + str(avg_max_displacement) + " Meters"
	plt.plot(dx_times[:len(stitched_location)], stitched_location_offset_adj, label='displacement')
	plt.ylabel('Displacement (m)')
	plt.xlabel('Time (Seconds)')
	plt.legend()
	plt.show()
	
	
def detrend_data(dx_times, velocity, location):
	plt.plot(dx_times[:-1], signal.detrend(velocity), label='velocity')
	plt.legend()
	plt.show()

	
def find_peaks(filtered_z_axis):
	peaks, properties = signal.find_peaks(-filtered_z_axis)#, prominence=(None, 1)
	#print properties["prominences"].max()
	#plt.plot(-filtered_z_axis, label='filtered z-axis acceleration')
	thresh_peaks = []
	for x in peaks:
		val = -filtered_z_axis[x]
		if  val > 2:
			thresh_peaks.append(x)
		
	#plt.plot(thresh_peaks, -filtered_z_axis[thresh_peaks], "x")
	#plt.legend()
	#plt.show()
	
	return thresh_peaks  ##return all peaks above specified threshold
		


### plot the data ###

def plot_data(z_accels, filtered_z_axis, velocity, location, dx_times):
	#plt.plot(dx_times, z_accels, label='z-axis acceleration')
	plt.plot(dx_times, filtered_z_axis, label='filtered z-axis acceleration')
	#plt.plot(dx_times[:-1], velocity, label='z-axis velocity')
	#plt.plot(dx_times[:-2], location, label='location')
	plt.ylabel('Acceleration ($ms^{2}$)')
	plt.xlabel('Time (Seconds)')
	plt.legend()
	plt.show()


def example_plot1(): ## plots z accel, filtered z accel, velocity and location
	timestamps, z_accels = get_csv_data()[:2]
	dx_times = format_millis_to_xaxis(timestamps, 1000)
	filtered_z_axis = filter_accel_data(z_accels)
	velocity, location = double_integrate_data(filtered_z_axis, dx_times)
	plot_data(z_accels, filtered_z_axis, velocity, location, dx_times)
	
def example_plot2(): # plot displacement using peak detect to reset integration
	timestamps, z_accels = get_csv_data()[:2]
	dx_times = format_millis_to_xaxis(timestamps, 1000)
	filtered_z_axis = filter_accel_data(z_accels)
	velocity, location = double_integrate_data(filtered_z_axis, dx_times)
	peaks = find_peaks(filtered_z_axis)
	chunk_integrate(dx_times, z_accels, peaks)
	
	
	
def pitch_roll_to_direction():
	pass



#example_plot1()
example_plot2()
timestamps, z_accels = get_csv_data()[:2]
dx_times = format_millis_to_xaxis(timestamps, 1000)
filtered_z_axis = filter_accel_data(z_accels)

a = np.array(filtered_z_axis)
zero_crossings = np.where(np.diff(np.signbit(a)))[0]
print(zero_crossings)

velocity, location = double_integrate_data(filtered_z_axis, dx_times)
peaks = find_peaks(filtered_z_axis)
chunk_integrate(dx_times, filtered_z_axis, zero_crossings)
plot_data(z_accels, filtered_z_axis, velocity, location, dx_times)


