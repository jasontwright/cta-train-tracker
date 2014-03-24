# test.py
#
# Access the CTA Train Tracker and fetch information about the Sheridan Red Line stop and write that information to a file 'Sheridan.xml'.
#
# This request is keyed to only return 1 arrival

import urllib
u = urllib.urlopen('http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=26dd7d79ef8548648a163327672361ff&mapid=40080&max=1')
data = u.read()
f = open('Sheridan.xml', 'wb')
f.write(data)
f.close()
print('Wrote Sheridan.xml')
