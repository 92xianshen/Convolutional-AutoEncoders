from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import datasets
#dataset = datasets.load_iris()

#y = dataset.target

import numpy as np
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=10 ,max_iter=500, random_state=1).fit(X)
labels_pred = kmeans_model.labels_

a=metrics.normalized_mutual_info_score(labels_true, labels_pred)
print a