# coding=UTF-8

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontpath = '/usr/share/fonts/chinese/TrueType/ukai.ttf'
font = fm.FontProperties(fname=fontpath)

X0 = np.array([7, 5, 7, 3, 4, 1, 0, 2, 8, 6, 5, 3])
X1 = np.array([5, 7, 7, 3, 6, 4, 0, 2, 7, 8, 5, 7])
plt.figure()
plt.axis([-1, 9, -1, 9])
plt.grid(True)
plt.title(u'原始分布圖', fontproperties=font)
plt.plot(X0, X1, 'k.')

C1 = [1, 4, 5, 9, 11]
C2 = list(set(range(12)) - set(C1))
X0C1, X1C1 = X0[C1], X1[C1]
X0C2, X1C2 = X0[C2], X1[C2]
plt.figure()
plt.title(u'第一次迭代後聚類結果', fontproperties=font)

plt.axis([-1, 9, -1, 9])
plt.grid(True)
plt.plot(X0C1, X1C1, 'rx')
plt.plot(X0C2, X1C2, 'g.')
plt.plot(4, 6, 'rx', ms=12.0)
plt.plot(5, 5, 'g.', ms=12.0)

# 肘部法則
cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
cluster2 = np.random.uniform(3.5, 4.5, (2, 10))
X = np.hstack((cluster1, cluster2)).T
plt.figure()
plt.axis([0, 5, 0, 5])
plt.grid(True)
plt.plot(X[:, 0], X[:, 1], 'k.')

# 我们计算,值从1到10对应的平均畸变程度：
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

K = range(1, 10)
meandistortions = []

for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    meandistortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
plt.plot(K, meandistortions, 'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度', fontproperties=font)
plt.title(u'用肘部法则来确定最佳的K值', fontproperties=font)

plt.show()
