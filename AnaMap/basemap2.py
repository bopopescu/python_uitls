import matplotlib
import numpy as np
from matplotlib.font_manager import FontProperties
matplotlib.use('TkAgg')
myfont = FontProperties(fname='/Library/Fonts/huawenfangsong.ttf')
matplotlib.rcParams['axes.unicode_minus']=False
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(11.7,8.3))
#Custom adjust of the subplots
plt.subplots_adjust(left=0.05,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
ax = plt.subplot(111)

#Let's create a basemap around Belgium
m = Basemap(resolution='i',projection='merc', llcrnrlat=10.0,urcrnrlat=55.0,llcrnrlon=60.,urcrnrlon=140.0)
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)

m.drawparallels(np.arange(10.,55.,10.),labels=[1,0,0,0],color='black',labelstyle='+/-',linewidth=0.2,dashes=(None, None)) # draw parallels,dashes=[1,0],
m.drawmeridians(np.arange(60.,140.,10.),labels=[0,0,0,1],color='black',labelstyle='+/-',linewidth=0.2,dashes=(None, None)) # draw meridians ,dashes=[1,0]
m.bluemarble()
plt.show()