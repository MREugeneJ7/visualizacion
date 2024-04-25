from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# generate synthetic two-dimensional data
X, y = make_blobs(random_state=1)

print("Shape X: {}".format(X.shape))
print("Data X: \n{}".format(X[0:5]))


# build the clustering model
kmeans = KMeans(n_clusters=3)  # 3 - clusters
kmeans.fit(X)

# During the algorithm, each training data point in X is assigned a cluster label. 
# You can find these labels in the kmeans.labels_ attribute
print("Cluster memberships:\n{}".format(kmeans.labels_))


# The cluster centers are stored in the cluster_centers_ attribute
print("Cluster centers:\n{}".format(kmeans.cluster_centers_))

# Predict asigna una etiqueta a un nuevo punto
# Running predict on the training set returns the same result as labels_

print("Running predict over the training set:\n{}".format(kmeans.predict(X)))

