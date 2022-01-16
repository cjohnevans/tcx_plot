# tcxpowercomp.py
# cje 15/1/2021
# load in two txc files with power data
# use forked version from https://github.com/vkurup/python-tcxparser

import sys
sys.path.append('/home/john/code/python-tcxparser/tcxparser')

import tcxparser
import matplotlib.pyplot as plt

tcx_garminvector = '/home/john/code/tcx_plot/activity_8120026129.tcx'
tcx_bikeerg = '/home/john/code/tcx_plot/activity_8120026129.gpx'

class ActivityData:
    def __init__(self, tcx_file):
        tcx = tcxparser.TCXParser(tcx_file)
        self.time = tcx.time_values()
        self.altitude = tcx.altitude_points()
        self.distance = tcx.distance_values()
        self.hr = tcx.hr_values()
        self.np = len(self.time)
        self.dt = tcx.time_durations()  # datetime.timedelta object
        # need to dt to be a sensible type in sensible units (float in sec, min?)
        print(self.np)

ride_garmin = ActivityData(tcx_garminvector)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.plot(ride_garmin.hr)
plt.show()

print(ride_garmin.dt[:100])
print(type(ride_garmin.dt[0].seconds))
print(ride_garmin.dt[20].seconds)
print(ride_garmin.dt[20].microseconds)

