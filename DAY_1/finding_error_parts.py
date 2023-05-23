#Finding error parts depend on dimensions

from sklearn import tree

#[x_lenght, y_lenght, z_lenght]

#technical drawing dimensions [12,20,11]

X = [[12.1,20.2,11.3],[11.9,22,10.0],[12,20.1,11],[12,20.1,11],[12,21,10.3],[13,23,11.1],[11.9,20,11.2],[12,20,11],[12,20,11]]

Y = ["Correct","Error","Correct","Error","Error","Error","Correct","Correct","Correct"]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

predict = clf.predict([[12.1,20,11]]) 
print(predict) #Gives ['Correct']
predict = clf.predict([[12.1, 23, 11]])
print(predict) #Gives ['Error']



#Tomorrow I will make connection to excel spreedsheets