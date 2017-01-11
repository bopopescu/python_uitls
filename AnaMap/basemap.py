import matplotlib
from matplotlib.font_manager import FontProperties
matplotlib.use('TkAgg')
myfont = FontProperties(fname='/Library/Fonts/huawenfangsong.ttf')
matplotlib.rcParams['axes.unicode_minus']=False

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


#程序输入是4个经度纬度参数，表示绘制范围，默认的纬度范围是17.25到20.25度，经度范围是-75到-71度。
def basic_map_plot(ax=None, lllat=17.25, urlat=20.25,
                    lllon=-75, urlon=-71):
    # 创建极球面投影的Basemap实例，projection='stere'表示地图类型是极球面，lon_0和lat_0表示地图中心点.



    m = Basemap(ax=ax, projection='stere',
                lon_0=(urlon + lllon) / 2,
                lat_0=(urlat + lllat) / 2,
                llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon,
                resolution='f')

    m.drawcoastlines() #绘制海岸线
    m.drawstates() #绘制州界
    m.drawcountries() #绘制国界
    #m.bluemarble()
    return m

basic_map_plot(None , 10 ,10 ,10,10)
plt.show()
