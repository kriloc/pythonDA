# coding=UTF-8
__author__ = 'krilo'

################# Sample 1 #################
"""
使用問卷調查看出相關係數
"""

from numpy import genfromtxt
from scipy.stats import pearsonr
import numpy as np
import pprint
import pandas as pd

datapath = r"調查顧客分類.csv"
deliveryData = genfromtxt(datapath, delimiter=",", skip_header=1)

print "資料集: \n價格,體力,零用錢,韓國料理,活力,特別,離車站近,豐富,方便,易找,桌子\n", deliveryData

"""
scipy.stats.pearsonr(x, y)[source]
x : (N,) array_like Input
y : (N,) array_like Input
Returns:
(Pearson’s correlation coefficient, 2-tailed p-value)

"""
datapath1 = r"調查顧客分類.xls"
pdata = pd.read_excel(datapath1)
# pdata = pd.Series(deliveryData, index=1)
# print pdata.corr()

# print pdata
# x = deliveryData[:, -1]  # 第一個參數指取多少行，第二個參數指取多少列
# print x
# y = deliveryData[-1, :]
# print y
# print pearsonr(x, y)
# result = np.corrcoef(deliveryData)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(pdata.corr())
