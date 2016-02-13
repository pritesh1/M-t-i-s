import json
import urllib
import urllib2
import matplotlib.pyplot as plt

url = 'https://api.github.com/repos/mbostock/d3/stats/commit_activity'
data=json.load(urllib2.urlopen(url))

max = 0
week = 0

for i in range(0,len(data)-1):
	#print data[i]['total']
	if (data[i]['total'] >= max):
		max = data[i]['total']
		week = i
print "week="+ str(week)
print "total=" + str(max)

plt.plot(data[37]['days'])

M =[]
N=[]
for i in range(0,len(data)-1):
	N.append(data[i]['total']
	for j in range (0,len(data[0]['days'])-1):
		M.append(data[i]['days'][j])
		
print M	
