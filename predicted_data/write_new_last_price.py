import datetime
import yfinance as yf
import pandas as pd

def write_new_last_price(crypto_name_list,crypto_name):
    
    
    
    Start_last_day = datetime.datetime.today() - datetime.timedelta(days=1)
    Start_last_day = Start_last_day.strftime("%Y-%m-%d")
    End_last_day   = datetime.datetime.today() - datetime.timedelta(days=0)
    End_last_day   = End_last_day.strftime("%Y-%m-%d")
    
    df_last_day = yf.download(crypto_name_list[crypto_name]+"-USD",start = Start_last_day,end =End_last_day)


    Last_Price_Data = pd.read_csv('predicted_data/Last_Price.csv')
    # Last_Price_Data.iloc[day, [index_of_crypto+1]] = predict[0]


    #if data is note updated get last row of minuts of yster day
    if df_last_day.size == 0  :
        print ('🚩🚩🚩🚩🚩🚩 THE DATA IS NOT UPDATED YET')



    Last_Price_Data['Date']= Start_last_day
    Last_Price_Data[crypto_name_list[crypto_name]]= df_last_day.Close[-1]
    Last_Price_Data.to_csv("predicted_data/Last_Price.csv",index=False)