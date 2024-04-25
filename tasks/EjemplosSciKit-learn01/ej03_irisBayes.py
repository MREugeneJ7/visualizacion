# Standard scientific Python imports
import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))

# Imprimir matriz de confusion -------------------------------------

print("Classification report for classifier %s:\n%s\n"
      % (gnb, metrics.classification_report(y_test, y_pred)))
#disp = metrics.plot_confusion_matrix(gnb, X_test, y_test, normalize = 'true')
disp = metrics.plot_confusion_matrix(gnb, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print("Confusion matrix:\n%s" % disp.confusion_matrix)

plt.show()
