# coding=UTF-8

from pandas.io.parsers import read_csv
import numpy as np

"""
pandas :
Series - 具有標籤(通常稱為索引)， 有 index 的 list
DataFrame - 有index 的 Series集合

"""

df = read_csv("data/WHO_first9cols.csv")
# print "DataFrame:/n", df
print "行列數：\n", df.shape
print "Length:", len(df)

country_col = df["Country"]
print "Country: \n", country_col
print "Type df", type(df)
print "Type country col", type(country_col)  # 可以看到country_col為Series型別


# print "Series shape", country_col.shape
# print "Series index", country_col.index
# print "Series values", country_col.values
print "Series name: ", country_col.name
#
print "Last 2 countries: \n", country_col[-2:]
# print "Last 2 countries type", type(country_col[-2:])
#
print "df signs: \n", np.sign(df)
last_col = df.columns[-1]
# print "Last df column signs: \n", last_col, np.sign(df[last_col])
#
# print np.sum(df[last_col] - df[last_col].values)
