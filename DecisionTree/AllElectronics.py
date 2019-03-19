#-*- coding:utf-8 -*-
'''
Created on Jan 4, 2019

@author: jyp
'''
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
#from sklearn.external.six import StringIO
allElectronicsData = open(r'./AllElectronics.csv')
reader = csv.reader(allElectronicsData)
headers = reader.next()
print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1,len(row)-1):
        #print(row[i])
        rowDict[headers[i]] = row[i]
        #print("rowDic",rowDict)
    featureList.append(rowDict)
print(featureList)

# Vector features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX:" + str(dummyX))
print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer();
dummyY = lb.fit_transform(labelList)
print("dummyY"+str(dummyY))


#Using decision tree for calssification
#clf = tree.DecesionTreeClassfier()
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX,dummyY)
print("clf:"+str(clf))



























