import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime

with open('stats.csv', 'r') as stats:
    stats=stats.read().splitlines()
download, upload, timestamps = zip(*[[int(xx) for xx in x.split('|')] for x in stats])
download = [int(x) / (1024*1024*1024) for x in download]
upload = [int(x) / (1024*1024*1024) for x in upload]
buffer = [x-y for x,y in zip(upload,download)]

freq_series = pd.Series.from_array(download)
freq_series2 = pd.Series.from_array(upload)
freq_series3 = pd.Series.from_array(buffer)

ax = freq_series.plot(label='download')
ax = freq_series2.plot(label='upload')
ax = freq_series3.plot(label='buffer')

ax.set_title("[REDACTED] statistics")
ax.set_xlabel("timestamps")
ax.set_ylabel("GiB")

timestamps=[datetime.datetime.fromtimestamp(TS).strftime('%Y-%m-%d') for TS in timestamps]

##ax.set_xticks(np.arange(len(timestamps)))
ax.set_xticklabels(timestamps)
ax.grid(True)
rects = ax.patches

plt.xticks( rotation=45 )
plt.legend()
plt.show()

#generate example stats
##import time, random
##
##basedl=311772993921
##baseul=405600045181
##t=int(time.time())
##def ranstats():
##    global basedl
##    global baseul
##    global t
##    basedl+=random.randint(100000000, 900000000)
##    baseul+=random.randint(10000000, 90000000)
##    t+=86400
##with open('stats.csv', 'w') as stats:
##    for x in range(100):
##        ranstats()
##        stats.write('{}|{}|{}\n'.format(basedl,baseul,t))
