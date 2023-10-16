from datetime import datetime
import pandas as pd



def write_requesting_list(customer_ID,Crypto_Stock,Prediction_In_Date,last_price,Prediction):

    requesting_list = pd.read_csv('request_handle/requesting_list.csv')


    #add new requist
    now = datetime.now()
    Request_Date = now.strftime("%Y-%m-%d %H:%M:%S")

    Customer_Id = customer_ID

    Crypto_Stock = Crypto_Stock

    Prediction_In_Date = Prediction_In_Date

    Prediction = Prediction

    

    new_row = {'Request_Date'       : [Request_Date],
               'Customer_Id'        : [Customer_Id],
               'Crypto/Stock'       : [Crypto_Stock],
               'Prediction_In_Date' : [Prediction_In_Date],
               'Last_Price'         : [last_price],
               'Prediction'         : [Prediction]
              }
    new_row = pd.DataFrame(new_row)

    requesting_list = pd.concat([requesting_list, new_row], ignore_index = True)
    requesting_list.to_csv("request_handle/requesting_list.csv",index=False)
    
    