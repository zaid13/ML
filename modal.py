from sklearn import tree

# x =[height, weight, shoe_size]
x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]


y = ['male','female','male',
    'female','male','female',
    'male','female','male',
    'female','male',]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)


print(str(clf.predict([[200,80,40]])) + '1')
print(str(clf.predict([[110,80,40]]))+ '2')
print(str(clf.predict([[200,80,25]]))+ '3')
print(str(clf.predict([[150,65,35]]))+ '4')