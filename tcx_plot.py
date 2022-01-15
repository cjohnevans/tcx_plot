# tcxpowercomp.py
# cje 15/1/2021
# load in two txc files with power data
# use forked version from https://github.com/vkurup/python-tcxparser

##import importlib
##spec=importlib.util.spec_from_file_location('tcxparser', \
##                            '/home/john/code/python-tcxparser/tcxparser/tcxparser.py')
##
##tcxparser = importlib.util.module_from_spec(spec)
##spec.loader.exec_module(tcxparser)

import sys
sys.path.append('/home/john/code/python-tcxparser/tcxparser')

import tcxparser
import matplotlib.pyplot as plt

tcxfile1 = '/home/john/code/tcxpowercomp/activity_8120026129.tcx'

tcx = tcxparser.TCXParser(tcxfile1)

class ActivityData:
    time = tcx.time_values()
    altitude = tcx.altitude_points()
    distance = tcx.distance_values()
    hr = tcx.hr_values()

ride_garmin = ActivityData()

fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.plot(ride_garmin.hr)
plt.show()

print (ride_garmin.hr[:100])
