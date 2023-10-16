import pandas as pd

from sklearn import neighbors, metrics
from sklearn.ensemble import RandomForestClassifier

from Applying_ML_Model.splitting_data import split_data




def final_training(name,df,daye):
    
    
    
    #split target and 
    
    X_train, X_test, y_train, y_test = split_data(df)
    
    
    
    print('\n')

    #####           RANDOM FOREST
    #==========================================applaying random forest

    from sklearn.ensemble import RandomForestClassifier
    # Instantiate model with 10 decision trees
    model_RF = RandomForestClassifier(n_estimators = 200 , random_state = 17)#23


    # Train the model on training data fit
    model_RF.fit(X_train, y_train)

    #prediction_test
    prediction_test = model_RF.predict(X_test)
    #print(y_test, prediction_test,'\n')

    #Accuracy
    from sklearn import metrics
    
    #Print the prediction accuracy
    print ("Random Forest Accuracy = ", metrics.accuracy_score(y_test, prediction_test),'   for   ',daye,'  dayes','\n')

    print('_____________________________','\n')
    
    
    
    
    # #==========================================applaying KNN
    #
    # model_KNN = neighbors.KNeighborsClassifier(n_neighbors= 3,weights ='uniform')
    #
    # model_KNN.fit(X_train, y_train)
    #
    # #predictions
    # prediction = model_KNN.predict(X_test)
    # #accuracy
    # accuracy_KNN = metrics.accuracy_score(y_test,prediction)
    #
    #
    #
    # #print("KNN prediction : ",prediction)
    # print("KNN accuracy            = ",accuracy_KNN ,'   for   ',daye,'  dayes','\n')
    print('=======================================================','end training data : ',name,'  for :',daye,'  dayes' ,'=======================================================','\n')

    
    
    
    
    return model_RF