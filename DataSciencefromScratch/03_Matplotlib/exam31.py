# coding=UTF-8
__author__ = 'krilo'

from matplotlib import pyplot as plt
import matplotlib.font_manager as fm

fontpath = '/usr/share/fonts/chinese/TrueType/ukai.ttf'
myfont = fm.FontProperties(fname=fontpath)

years =[1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("GDP")
plt.ylabel(u"十億美金", fontproperties=myfont)
plt.show()

# plt.savefig('test3.png')