import csv
import scipy.integrate as it
import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sys
from numpy import median





### open csv file and get required parameters ###
###csv format : (lin accel) X, Y, Z, (Euler) X, Y, Z, (MAG) X, Y , TIMESTAMP######


def get_csv_data():
	timestamps = []
	z_accels   = []
	pitch      = []
	roll       = []
	with open('20cm_datalog.csv', 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			row = row[:-1]
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

	len_array = len(peaks)
	
	print len (dx_times)
	print len (filtered_z_axis)
	
	#use the peaks index numbers to split the z_accels and x_axis times into chunks
	for idx in range(len_array-1):  
		z_accels_chunks.append(filtered_z_axis[peaks[idx]:peaks[idx+1]])
		x_axis_chunks.append(dx_times[peaks[idx]:peaks[idx+1]])
		
	
	
	#double integrate each of the z_accel chunks to get velocity chunks
	
	for h,g in zip(z_accels_chunks[0], z_accels_chunks[1]):
		print h,g
	
	
	print "........."
	
	for x,y in zip(z_accels_chunks, x_axis_chunks):
		print x[0],x[-1],y[0],y[-1]
	
	print dx_times[peaks[0]]
	print dx_times[peaks[-1]]
	
	for idx, h in enumerate(x_axis_chunks):
		
		velocity_chunk.append(it.cumtrapz(z_accels_chunks[idx],h))
		location_chunk.append(it.cumtrapz(remove_dc_offset(velocity_chunk[-1]),h[:-1]))
	
	plt.subplot(3, 1, 1)	
	plt.ylabel('Acceleration (ms^-2)')
	for loc,x in zip(z_accels_chunks, x_axis_chunks):
		print loc[0],loc[-1],x[0],x[-1]
		plt.plot(x[:len(loc)], loc, "--")
		
	xcoords = []
	for h in x_axis_chunks:
		xcoords.append(h[0])
	for xc in xcoords:
		plt.axvline(x=xc)
		
	
	plt.subplot(3, 1, 2)
	plt.ylabel('Velocity (m/s)')
	
	for h in x_axis_chunks:
		xcoords.append(h[0])
	for xc in xcoords:
		plt.axvline(x=xc)
	
	for loc,x in zip(velocity_chunk, x_axis_chunks):
		print loc[0],loc[-1],x[0],x[-1]
		plt.plot(x[:len(loc)], remove_dc_offset(loc), "--")
		
	plt.subplot(3, 1, 3)
	plt.ylabel('Displacement (m)')
	xcoords = []
	for h in x_axis_chunks:
		xcoords.append(h[0])
	for xc in xcoords:
		plt.axvline(x=xc)
	for loc,x in zip(location_chunk, x_axis_chunks):
		print loc[0],loc[-1],x[0],x[-1]
		plt.plot(x[:len(loc)], loc, "o")
	
	#for loc,x in zip(z_accels_chunks, x_axis_chunks):
	#	print loc[0],loc[-1],x[0],x[-1]
	#	plt.plot(x[:len(loc)], loc, "x")
	
#	myzip = zip(x_axis_chunks[1],location_chunk[1])
#	for h in myzip:
#		print h
	
	stitched_location = []
	stitched_velocity = []
	max_heights       = []
	min_heights       = []
	displacements     = []
	
	
	#check each chunk for the max displacement in that chunk
	for h in location_chunk:
		max_heights.append(float(max(h)))
		min_heights.append(float(min(h)))
		displacements.append(abs(max(h))+abs(min(h)))

		
	print displacements
	avg_max_displacement =  (sum(max_heights) / float(len(max_heights)))
	avg_min_displacement =  (sum(min_heights) / float(len(min_heights)))
	
	#print avg_max_displacement, avg_min_displacement
	#print avg_max_displacement + abs(avg_min_displacement)
	avg_displacement =  sum(displacements) / float(len(displacements))
	median_displacement =  median(displacements)
	
	
	
	#stitch all of the chunks together	
	for x in location_chunk:
		for y in x:
			stitched_location.append(y)
			
	for x in velocity_chunk:
		for y in x:
			stitched_velocity.append(y)
			
	#get the average displacement of the data and remove any offset present
	displacement_offset =  sum(stitched_location) / float(len(stitched_location))
	displacement_offset = -displacement_offset
	stitched_location_offset_adj = []	
	for h in stitched_location:
		stitched_location_offset_adj.append(h + float(displacement_offset))
		
	print len(stitched_location)
	print "Median Displacement = " + str(median_displacement) + " Meters"		
	print "Average Chunk Displacement = " + str(avg_displacement) + " Meters"
#	plt.plot(dx_times[:len(stitched_location)], stitched_location, "o", label='displacement')
	
	xcoords = []
	for h in x_axis_chunks:
		xcoords.append(h[0])
	for xc in xcoords:
		plt.axvline(x=xc)
		
	#plt.plot(dx_times[:len(stitched_velocity)], stitched_velocity, "x", label='velocity')
	#plt.ylabel('Displacement (m)')
	plt.xlabel('Time (Seconds)')
	plt.legend()
	plt.show()
	
	
def detrend_data(dx_times, velocity, location):
	plt.plot(dx_times[:-1], signal.detrend(velocity), label='velocity',)
	plt.legend()
	plt.show()

	
def find_peaks(filtered_z_axis):
	all_peaks=[]
	thresh_peaks=[]
	peaks1, properties1 = signal.find_peaks(-filtered_z_axis)#, prominence=(None, 1)
	#peaks2, properties2 = signal.find_peaks(filtered_z_axis)
	
	
	for h in peaks1:
		all_peaks.append(h)
	#for h in peaks2:
	#	all_peaks.append(h)
		
	
	
	
	thresh_peaks = sorted(all_peaks)
	
	#print properties["prominences"].max()
	#plt.plot(-filtered_z_axis, label='filtered z-axis acceleration')
	#thresh_peaks = []
	#for x in peaks:
	#	val = -filtered_z_axis[x]
		#if  val > 0.4:
	#	thresh_peaks.append(x)
		
	
	plt.plot(filtered_z_axis, label='filtered z-axis acceleration')
	plt.plot(thresh_peaks, filtered_z_axis[thresh_peaks], "x")
	plt.legend()
	plt.show()
	
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

def remove_dc_offset(data): # calculates average and removes any offset from dataset
	output = []
	avg = sum(data) / len(data)
	#print "average = " + str(avg)
	avg = -avg
	
	for h in data:
		output.append(h+avg)
	return output

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
	chunk_integrate(dx_times, filtered_z_axis, peaks)
	
	
	
def pitch_roll_to_direction():
	pass
	
def make_sine_wave():
	Fs = 20
	f = 0.2
	sample = 462
	x = np.arange(sample)
	y = (0.3*np.sin((2 * np.pi * f * x / Fs)))-0.3
	return y
	#plt.plot(x, y)
	#plt.xlabel('sample(n)')
	#plt.ylabel('voltage(V)')
	#plt.show()



example_plot1()
#example_plot2()
timestamps, z_accels = get_csv_data()[:2]
dx_times = format_millis_to_xaxis(timestamps, 1000)
filtered_z_axis = filter_accel_data(z_accels)

#filtered_z_axis = make_sine_wave()
a = np.array(filtered_z_axis)
zero_crossings = np.where(np.diff(np.signbit(a)))[0]
print(zero_crossings)

velocity, location = double_integrate_data(filtered_z_axis, dx_times)
peaks = find_peaks(filtered_z_axis)
print peaks
#chunk_integrate(dx_times, remove_dc_offset(z_accels), zero_crossings)
chunk_integrate(dx_times, remove_dc_offset(filtered_z_axis), peaks)
#plot_data(remove_dc_offset(filtered_z_axis), filtered_z_axis, velocity, location, dx_times)



