This is data taken from the BN055 9 Degrees of Freedom IMU device.

The format is as follows:

linaccel x, linaccel y, linaccel z, euler x, euler y, euler z, mag x, mag y

linaccel = linear acceleration (acceleration with gravity removed)
euler    = euler angles for x,y, and z axes
mag      = magnetometer values for x and y axes

The name of the file refers to the radius used for the rotating arm test. Theoretically the maximum displacement should be twice this value. The 
second digit in the name refers to the voltage applied to the motor which rotated the arm. It was not possible to control for frequency and two 
voltages 3v and 4.5v were used at each radius just to give two different speeds.
