import datetime

depthlist = []
i = 0
depthtotime = []
for line in open('/ufrc/zoo6927/share/pcfb/examples/ctd.txt'):
    i += 1
    if i > 1:
        items = line.strip().split(',')
        timedate = items[1]
        depth = float(items[4])
        depthlist.append(depth)
        time = timedate[11:]
        hours = int(time[:2])
        minutes = int(time[3:5])
        seconds = int(time[6:8])
        totalminutes = (hours*6)+minutes
        totalseconds = (totalminutes*60)+seconds
        depthtotime.append([totalseconds, depth])

i = 0 
for item in depthtotime:
    
    if i == 0:
        starttime = item[0]
    i += 1
    if item[1] > 80.0:
        endtime = item[0]
        break

timeto80 = endtime-starttime
minutes = timeto80/60
seconds = timeto80%60

print 'The time to get to 80 meters is: ', minutes,'minutes',seconds, 'seconds'

start80 = []
i = 0

for item in depthtotime:
    
    if item[1] > 80.0:
        start80.append(item[0])
    
timeover80 = start80[-1] - start80[0]
minutes = timeover80/60
seconds = timeover80%60

print 'The time over 80 meters is: ',  minutes,'minutes',seconds,'seconds'

maxval = max(depthlist)

f = open('/ufrc/zoo6927/share/lancetdenes/submarine/maxdepth.txt', 'w')

f.write('The Max depth is: %s'%(maxval))

