# coding=UTF-8
__author__ = 'krilo'

from matplotlib import pyplot as plt
import matplotlib.font_manager as fm

fontpath = '/usr/share/fonts/chinese/TrueType/ukai.ttf'
myfont = fm.FontProperties(fname=fontpath)

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel(u"朋友數", fontproperties=myfont)
plt.ylabel(u"花在網站上的日分鐘數", fontproperties=myfont)
plt.show()
