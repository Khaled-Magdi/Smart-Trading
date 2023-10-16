from datetime import datetime
import pandas as pd
from request_handle.update_requist_list import write_requesting_list



def customer_request_handling(customer_ID,crypto_stock_name,predect_in_date):
    
    prediction_Data = pd.read_csv('predicted_data/prediced_data.csv')
    last_price_Data = pd.read_csv('predicted_data/Last_Price.csv')

#     predect_date = datetime.strptime(predect_date,"%Y-%m-%d").date()
#     predect_date = str(predect_date)


    #to get prediction from prediction sheet
    crypto_names = ['BTC','ETH','BNB','XRP','SOL','CHZ','STETH']
    crypto_name_index = crypto_names.index(crypto_stock_name)

    data_row = prediction_Data.loc[prediction_Data['Date'] == predect_in_date]
    predect = data_row.iloc[0, crypto_name_index+1]


    #to get last price from last_price sheet
    last_price = last_price_Data.iloc[0, crypto_name_index+1]



    write_requesting_list(customer_ID,crypto_stock_name,predect_in_date,last_price,predect)

    
    
    return predect,last_price



