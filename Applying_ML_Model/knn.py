from sklearn import neighbors, metrics

def knn_model(X_train, X_test, y_train, y_test,daye):

    knn = neighbors.KNeighborsClassifier(n_neighbors= 3,weights ='uniform')

    knn.fit(X_train, y_train)

    #predictions
    prediction = knn.predict(X_test)
    #accuracy
    accuracy = metrics.accuracy_score(y_test,prediction)


    
    #print("KNN prediction : ",prediction)
    print("KNN accuracy : ",accuracy ,'   for   ',daye,'  dayes','\n')
    print('========================================================================================','\n')

    return knn