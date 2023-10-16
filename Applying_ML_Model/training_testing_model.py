from Applying_ML_Model.splitting_data import split_data
from Applying_ML_Model.random_forest import random_forest_model
from Applying_ML_Model.knn import knn_model


#function to splitting data train_test
def train_test_model(df_day, df_week, df_month):

    #============================================================== 1 day ===========================
    # call fun to splitting data
    X_train_d, X_test_d, y_train_d, y_test_d = split_data(df_day)
    # call fun to applaying RANDOM FOREST model
    Random_forest_model_day = random_forest_model(X_train_d, X_test_d, y_train_d, y_test_d,1)
    # call fun to applaying kNN model
    KNN_model_day = knn_model(X_train_d, X_test_d, y_train_d, y_test_d,1)



    #============================================================== 7 day ===========================
    # call fun to splitting data
    X_train_w, X_test_w, y_train_w, y_test_w = split_data(df_week)
    # call fun to applaying RANDOM FOREST model
    Random_forest_model_week = random_forest_model( X_train_w, X_test_w, y_train_w, y_test_w,7)
    # call fun to applaying kNN model
    KNN_model_week = knn_model(X_train_w, X_test_w, y_train_w, y_test_w,7)




    #============================================================== 30 day ===========================
    # call fun to splitting data
    X_train_m, X_test_m, y_train_m, y_test_m = split_data(df_month)
    # call fun to applaying RANDOM FOREST model
    Random_forest_model_month = random_forest_model( X_train_m, X_test_m, y_train_m, y_test_m,30)
    # call fun to applaying kNN model
    KNN_model_month = knn_model(X_train_m, X_test_m, y_train_m, y_test_m,30)
    
    
    return Random_forest_model_day, Random_forest_model_week, Random_forest_model_month