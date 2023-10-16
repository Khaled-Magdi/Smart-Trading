import pandas as pd

from sklearn.ensemble import RandomForestClassifier

def random_forest_model( X_train, X_test, y_train, y_test,daye):
    print('\n')

    #####           RANDOM FOREST
    #applaying random forest

    from sklearn.ensemble import RandomForestClassifier
    # Instantiate model with 10 decision trees
    model = RandomForestClassifier(n_estimators = 200 , random_state = 17)#23


    # Train the model on training data fit
    model.fit(X_train, y_train)

    #prediction_test
    prediction_test = model.predict(X_test)
    #print(y_test, prediction_test,'\n')

    #Accuracy
    from sklearn import metrics
    #Print the prediction accuracy
    print ("Random Forest Accuracy = ", metrics.accuracy_score(y_test, prediction_test),'   for   ',daye,'  dayes','\n')

    #importance featuer

    print('_____________________________','\n')
    
    return model