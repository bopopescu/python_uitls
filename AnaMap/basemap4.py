作者：何明涛
链接：https: // www.zhihu.com / question / 49669755 / answer / 117962271
来源：知乎
著作权归作者所有，转载请联系作者获得授权。

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
bmap = Basemap(llcrnrlon=115, llcrnrlat=23, urcrnrlon=121, urcrnrlat=29,
               projection='lcc', lat_1=33, lat_2=45, lon_0=120, ax=ax1)
shp_info = bmap.readshapefile('CHN_adm/CHN_adm3', 'states', drawbounds=False)

for info, shp in zip(bmap.states_info, bmap.states):
    proid = info['NAME_1']
    if proid == 'Fujian':
        poly = Polygon(shp, facecolor='w', edgecolor='b', lw=0.2)
        ax1.add_patch(poly)

bmap.drawcoastlines()
bmap.drawcountries()
bmap.drawparallels(np.arange(23, 29, 2), labels=[1, 0, 0, 0])
bmap.drawmeridians(np.arange(115, 121, 2), labels=[0, 0, 0, 1])
plt.title('Fujian Province')
plt.savefig('fig_province.png', dpi=100, bbox_inches='tight')
plt.clf()
plt.close()