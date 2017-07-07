from sklearn import svm
import numpy as np


class Predict:

    def read(self,dir):
        x = []
        y = []
        with open(dir) as f:
            lines = f.readlines()
        for i in range(len(lines)):
            y.append(lines[i][0]);x.append(lines[i][1:])
        y = np.array([[float(i)] for i in y])
        x = np.array([[float(i)] for i in x])

        return x,y


    def Svm(self,value,feature,target):
        clf = svm.SVC()
        clf.fit(feature,target)
        return int(clf.predict([value]))

    def Tresh(self,opEar):
        if opEar > 0.2: return True
        else: return False
