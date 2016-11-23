from sklearn import tree
features = [[140, 0], [130, 0], [150, 1], [170, 1]]  # 0 = bumpy, 1 = smooth
labels = [0, 0, 1, 1]  # 0 = apple, 1 = orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[150, 0]])
