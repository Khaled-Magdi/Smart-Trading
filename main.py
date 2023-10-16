import pandas as pd
import time
import shutil
import datetime

from Handling_Data.mixing_data import download_mix_data
from Handling_Data.mixing_data import mix_data
from Handling_Data.preparing_data_to_predict import preparing_to_predect
from Handling_Data.preparing_last_days import preparing_last_60_day_data

from Applying_ML_Model.training_testing_model import train_test_model
from Applying_ML_Model.rf_knn_final_traning import final_training

from predicted_data.write_new_day_predict import write_new_day_predict
from predicted_data.update_data import update_prediction

from request_handle.reply_to_request import customer_request_handling




# #call download and prepaing data
# # call fun and download data in for loop
# Stocks = ['BTC','BNB','STETH','XRP','WBTC']
# df = download_mix_data(Stocks,1,'','')




#
# #call fun and load data in for loop
# Stocks = ['Stocks/BNB_all_time.csv',
#           'Stocks/BTC_all_time.csv',
#           'Stocks/STETH_all_time.csv',
#           'Stocks/WBTC_all_time.csv',
#           'Stocks/XRP_all_time.csv',]
# df_day = mix_data(Stocks,30)



# #lodding data arready prepared 1 day
# df_day = pd.read_csv('Stocks/all_data(daily).csv')
# #lodding data arready prepared 7 day
# df_week = pd.read_csv('Stocks/all_data(weekly).csv')
# #lodding data arready prepared 30 day
# df_month = pd.read_csv('Stocks/all_data(monthly).csv')
#
# #
# RF_day, RF_week, RF_month =train_test_model(df_day, df_week, df_month)



# #call function for all dayes
# for i in range(2,3):
#
#     print(i)
#     df1 = preparing_to_predect('data_csv/crypto_data_collection/CHZ/BTC.csv',days = i)
#     df2 = preparing_to_predect('data_csv/crypto_data_collection/CHZ/CHZ.csv',days = i)
#     df3 = preparing_to_predect('data_csv/crypto_data_collection/CHZ/STETH.csv',days = i)
#     df4 = preparing_to_predect('data_csv/crypto_data_collection/CHZ/WBTC.csv',days = i)
#     df5 = preparing_to_predect('data_csv/crypto_data_collection/CHZ/XRP.csv',days = i)
#
#
#
#     df = df1
#     df = df.append([
#                      df2,
#                      df3,
#                      df4,
#                      df5
#                     ])
#
#     #drop close
#     df.drop(['Close'], axis=1, inplace=True)
#     df.drop(['Market Cap'], axis=1, inplace=True)
#     print('len of all data = ',len(df))
#
#     df.to_csv(r'data_for_predict/crypto/CHZ/CHZ(file_to_predict_'+str(i)+'_day).csv', encoding='utf-8', index=False)
#
#
#     print ('=========================================round nuber  :',i , '  is done')
#     print ('============================================================================================================================')





# coin_trained = [CHZ_predict_RF_1_day,CHZ_predict_RF_2_day,CHZ_predict_RF_3_day,CHZ_predict_RF_4_day,CHZ_predict_RF_5_day,
#            CHZ_predict_RF_6_day,CHZ_predict_RF_7_day,CHZ_predict_RF_8_day,CHZ_predict_RF_9_day,CHZ_predict_RF_10_day,
#            CHZ_predict_RF_11_day,CHZ_predict_RF_12_day,CHZ_predict_RF_13_day,CHZ_predict_RF_14_day,CHZ_predict_RF_15_day,
#            CHZ_predict_RF_16_day,CHZ_predict_RF_17_day,CHZ_predict_RF_18_day,CHZ_predict_RF_19_day,CHZ_predict_RF_20_day,
#            CHZ_predict_RF_21_day,CHZ_predict_RF_22_day,CHZ_predict_RF_23_day,CHZ_predict_RF_24_day,CHZ_predict_RF_25_day,
#            CHZ_predict_RF_26_day,CHZ_predict_RF_27_day,CHZ_predict_RF_28_day,CHZ_predict_RF_29_day,CHZ_predict_RF_30_day]








# START_TIME = time.time()
#
#
#
#
# crypto_name = ['BTC','ETH','BNB','XRP','SOL','CHZ','STETH']
# folder_crypto_name = ['BTC_STETH_XRP_WPTC','ETH','BNB','BTC_STETH_XRP_WPTC','SOL','CHZ','BTC_STETH_XRP_WPTC']
# file_crypto_name = ['btcstethxrpwbtc-data','ETH','BNB','btcstethxrpwbtc-data','SOL','CHZ','btcstethxrpwbtc-data']
#
#
# update_prediction(crypto_name,folder_crypto_name,file_crypto_name)
#
#
#
# END_TIME = time.time()
# print('the run time is : ',int((END_TIME-START_TIME)/60),' min')





# #call request_handle
# predect,last_price = customer_request_handling('@Manager','BTC','2022-10-15')
# print('the output of prediction   =  ' , predect )
# print('the output of last price   =  ' , last_price,'\n')

