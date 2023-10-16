from sklearn.model_selection import train_test_split

#function to splitting data train_test
def split_data(df):

    #sellect X and Y data (Target)
    Y = df["Up_Down"]
    #Y=Y.astype('int')
    X = df.drop(labels = ["Up_Down"], axis=1)

    #splite train_test
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=7)


    return X_train, X_test, y_train, y_test