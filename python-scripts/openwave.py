import csv
import scipy.integrate as it
import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sys
from numpy import median
from scipy.fftpack import fft
import matplotlib.ticker as plticker
import os



### open csv file and get required parameters ###
###csv format : (lin accel) X, Y, Z, (Euler) X, Y, Z, (MAG) X, Y , TIMESTAMP######


def get_csv_data(filename):
	timestamps = []
	z_accels   = []
	pitch      = []
	roll       = []
	with open(filename, 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			#row = row[:-1]
			if row:
				
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
	#	print round( float(timestamps[idx+1])-float(timestamps[idx]) ,5)
		dx_time = round(dx_time, 8)
		dx_times.append(dx_time)
		
	
	return dx_times
	
### filter the acceleration data ###
def filter_accel_data(z_accels):
	fs = 19.23
	fc = 0.7  # Cut-off frequency of the filter (was 2)
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





### integrate the (acceleration) data in chunks ###
def chunk_integrate(dx_times, zdata, peaks):   
	data = remove_dc_offset(zdata)     
	data_chunks = []
	x_axis_chunks   = []
	zeroed_x_axis   = []
	velocity_chunks  = []
	location_chunks  = []

	len_array = len(peaks)
	
	#use the peaks index numbers to split the z_accels and x_axis times into chunks
	for idx in range(len_array-1):  
		data_chunks.append(data[peaks[idx]:peaks[idx+1]])
		x_axis_chunks.append(dx_times[peaks[idx]:peaks[idx+1]])
		
	#double integrate each of the acceleration chunks to get velocity chunks
	
	for idx, h in enumerate(x_axis_chunks):
		
		velocity_chunks.append(it.cumtrapz(data_chunks[idx],h))
		location_chunks.append(it.cumtrapz(remove_dc_offset(velocity_chunks[-1]),h[:-1]))
		
	return [velocity_chunks, location_chunks, data_chunks, x_axis_chunks]


# make a 3 in 1 plot with acceleration, velocity and displacement in chunk format

def chunk_plot(velocity_chunks, location_chunks, z_accels_chunks, x_axis_chunks):	
	
	
	plt.subplot(3, 1, 1)	
	plt.ylabel('Acceleration (ms^-2)')
	for loc,x in zip(z_accels_chunks, x_axis_chunks):
		plt.plot(x[:len(loc)], loc, "--")
		
	plt.subplot(3, 1, 2)
	plt.ylabel('Velocity (m/s)')
	for loc,x in zip(velocity_chunks, x_axis_chunks):
		plt.plot(x[:len(loc)], remove_dc_offset(loc), "--")
		
	plt.subplot(3, 1, 3)
	plt.ylabel('Displacement (m)')
	for loc,x in zip(location_chunks, x_axis_chunks):
		plt.plot(x[:len(loc)], loc, "o")
		
	plt.xlabel('Time (Seconds)')
	plt.legend()
	plt.show()


#look at chunks and determine median and average displacement

def chunk_analyze(chunks):
	stitched_chunks = []
	stitched_velocity = []
	max_heights       = []
	min_heights       = []
	displacements     = []
	
	
	#check each chunk for the max displacement in that chunk
	for h in chunks:
		max_heights.append(float(max(h)))
		min_heights.append(float(min(h)))
		displacements.append(abs(max(h))+abs(min(h)))

	
	avg_displacement =  sum(displacements) / float(len(displacements))
	median_displacement =  median(displacements)
	
	
	#print "Median Displacement = " + str(median_displacement) + " Meters"		
	print "Average Displacement = " + str(round(avg_displacement,4)) + " Meters"

	
#take seperate chunks and combine into a single list
	
def stitch_chunks(chunks):
	stitched_chunks = []
	for x in chunks:
		stitched_chunks.extend(x)
		
	return stitched_chunks

# take data with a linear offset and plot it with this offset removed

def detrend_data(dx_times, velocity, location):
	plt.plot(dx_times[:-1], signal.detrend(velocity), label='velocity',)
	plt.legend()
	plt.show()


# find peaks in a list and return the index numbers of the peaks

def find_peaks(data):
	all_peaks=[]
	thresh_peaks=[]
	#peaks1, properties1 = signal.find_peaks(np.negative(data))#, prominence=(None, 1)
	peaks2, properties2 = signal.find_peaks(data)
	
	
	#for h in (peaks1):
	#	all_peaks.append(h)
	
	for h in peaks2:
		if data[h]>0:
			all_peaks.append(int(h))

	thresh_peaks = sorted(all_peaks)
	
	for h in thresh_peaks:
		plt.plot(h, data[h], "x")

#	plt.plot(data, label='filtered z-axis acceleration')
	
	#plt.legend()
	#plt.show()
	
	return thresh_peaks  ##return all peaks above specified threshold
		


### various plots, comment lines on/off as required ###

def plot_data(z_accels, filtered_z_axis, velocity, location, dx_times):
	#plt.plot(dx_times, z_accels, label='z-axis acceleration')
	plt.plot(dx_times, filtered_z_axis, label='filtered z-axis acceleration')
	#plt.plot(dx_times[:-1], velocity, label='z-axis velocity')
	#plt.plot(dx_times[:-2], location, label='location')
	plt.ylabel('Acceleration ($ms^{2}$)')
	plt.xlabel('Time (Seconds)')
	plt.legend()
	plt.show()


# remove a dc offset from dataset and return list with offset removed

def remove_dc_offset(data): 
	output = []
	avg = sum(data) / len(data)
	#print "average = " + str(avg)
	avg = -avg
	
	for h in data:
		output.append(h+avg)
	return output

	
def pitch_roll_to_direction():
	pass

# return a list with generic sine wave for testing

def make_sine_wave():
	Fs = 20
	f = 0.2
	sample = 462
	x = np.arange(sample)
	y = (0.3*np.sin((2 * np.pi * f * x / Fs)))
	return y
	
# find zero crossings in list and return their index numbers
	
def get_zero_crossings(filtered_z_axis):
	a = np.array(filtered_z_axis)
	zero_crossings = np.where(np.diff(np.signbit(a)))[0]
	return zero_crossings	

# take accel data, chunk it, double integrate, plot and analyze
def measure_displacement_peak_detect(filename):
	timestamps, z_accels = get_csv_data(filename)[:2]                     # get timestamps and z accel data from csv file
	dx_times = format_millis_to_xaxis(timestamps, 1000)			  # format the timestamps into milliseconds and zero it	
	filtered_z_axis = filter_accel_data(z_accels)                 # filter the z accel data
	peaks = find_peaks(filtered_z_axis)							  # find the peaks	
	velocity_chunks, location_chunks, z_accels_chunks, x_axis_chunks  = chunk_integrate(dx_times,filtered_z_axis, peaks)  # take time and z axis data and peaks, cut data into chunks and integrate them seperately twice (to get velocity and location)
	#chunk_plot(velocity_chunks, location_chunks, z_accels_chunks, x_axis_chunks) #make a 3 in 1 plot with acceleration, velocity and displacement
	chunk_analyze(location_chunks)								  # look at each of the location chunks for max displacement etc.
	
	
def measure_displacement_zero_crossings(filename):
	timestamps, z_accels = get_csv_data(filename)[:2]
	dx_times = format_millis_to_xaxis(timestamps, 1000)
	filtered_z_axis = filter_accel_data(z_accels)
	zero_crossings = get_zero_crossings(filtered_z_axis)
	velocity_chunks, location_chunks, z_accels_chunks, x_axis_chunks  = chunk_integrate(dx_times, remove_dc_offset(filtered_z_axis), zero_crossings[::3])
	#chunk_plot(velocity_chunks, location_chunks, z_accels_chunks, x_axis_chunks)
	chunk_analyze(location_chunks)
	stitched_location = remove_dc_offset(stitch_chunks(location_chunks))

# perform an fft on input list and plot it
def fft(displacement):
	from scipy.fftpack import fft
	# Number of sample points
	N = len(displacement)
	# sample spacing
	
	yf = fft(displacement)
	print yf
	
	import matplotlib.pyplot as plt
	plt.plot(2.0/N * np.abs(yf[0:N//2]))
	plt.grid()
	plt.show()


def chunkify(dataset): #find peaks in dataset and break into chunks at those peaks
	new_chunks = []
	peaks = find_peaks(dataset)
	len_array = len(peaks)
	for idx in range(len_array-1):  
			new_displacement_chunks.append(dataset[peaks[idx]:peaks[idx+1]])
		
	return new_displacement_chunks

	
for h in os.listdir("test_data"):
	if h == "data_readme.txt": continue
	if "3v" in h            : continue
	measure_displacement_peak_detect("test_data/"+h)
	



