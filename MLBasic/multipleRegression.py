# coding=UTF-8
__author__ = 'krilo'

from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

datapath = r"data/multiRegression.csv"
deliveryData = genfromtxt(datapath, delimiter=",")

print "資料集: 英哩數, 運輸次數, 時間\n", deliveryData


x = deliveryData[:, :-1]  # 第一個參數指取多少行，第二個參數指取多少列
y = deliveryData[:, -1]
print "X:", x
print "Y:", y
regr = linear_model.LinearRegression()
regr.fit(x, y)

print "coefficients :", regr.coef_  # 公式中的b1 , b2, ....
print "regr.intercept_", regr.intercept_  # 截距

print "進行預測：假設運輸任務是跑102英哩，運輸6次，預計多少小時？"

xPred = [102, 6]
yPred = regr.predict(xPred)
print "yPred: ", yPred


