# coding=UTF-8
__author__ = 'krilo'

"""
使用 Numpy 進行基本的 平均數 / 中位數 / 最大最小值 / 標準差
資料有兩欄位: 國家 , 新病例百分比
country,e_new_mdr_pcnt
"""

import numpy as np
from scipy.stats import scoreatpercentile

data = np.loadtxt("data/mdrtb_2012.csv", delimiter=',', usecols=(1,), skiprows=1, unpack=True)

print "Max method", data.max()
print "Max Function", np.max(data)

print "Min method", data.min()
print "Min function", np.min(data)

print "Mean method", data.mean()
print u"平均值", np.mean(data)

print "Std method", data.std()
print "Std function", np.std(data)

print u"中位數Median", np.median(data)
print u"也叫50百分位点，因为有50%的观测值在它之下："
print "Score at percentile 50", scoreatpercentile(data, 50)

