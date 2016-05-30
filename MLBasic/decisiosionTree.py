# coding=UTF-8
__author__ = 'krilo'

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
import pprint


pp = pprint.PrettyPrinter(indent=4)

datapath = r"data/decisiosionExample.csv"
"""
該資料描述 年齡 / 收入 / 是否為學生 / 是否會購買電腦
"""

allElectronicsData = open(datapath, 'rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()

print "欄位:\n", headers

featuresList = []  # 已知的標籤，前五個欄位
labelList = []

for row in reader:
    # print "row:", row
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featuresList.append(rowDict)

pp.pprint(featuresList)

#  Vectorize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featuresList).toarray()
print "dummyX: "
pp.pprint(dummyX)

print labelList

# Vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)  # 將yes/ no 轉成 0/1
print "dummyY:"
pp.pprint(dummyY)

# Using decicsion tree for classification
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print "clf相關資訊:", str(clf)

# 繪出樹圖資訊 (不用每次都匯)
# with open("decisionTreeGain.dot", 'w') as f:
#     f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# 給予新的值來預測：
oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict(newRowX)
# print("predictedY: " + str(predictedY))
if predictedY == 1:
    print "會買"
else:
    print "不買"