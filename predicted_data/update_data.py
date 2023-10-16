#to writting new day predict in .csv sheat
import datetime
import pandas as pd
import pandas as pd
import shutil
import datetime

from Applying_ML_Model.rf_knn_final_traning import final_training
from predicted_data.write_new_day_predict import write_new_day_predict
from predicted_data.write_new_last_price import write_new_last_price






def update_prediction(crypto_name,folder_crypto_name,file_crypto_name) :


    for i in range(len(crypto_name)):

        for j in range(30):

            df = pd.read_csv('data_for_predict/crypto/'+folder_crypto_name[i]+'/'+file_crypto_name[i]+'_(file_to_predict_'+str(j+1)+'_day).csv')
            model_predicted = final_training(crypto_name[i],df,str(j))
            # BNB[i-1] = final_training('BNB',df,str(i))
            write_new_day_predict('predicted_data/prediced_data.csv',j,crypto_name[i],model_predicted,i)
        print('✓✓✓✓✓✓                                              ••••••••••••••••••the prediction is written•••••••••••••••••• ')








        #writting last price:
        write_new_last_price(crypto_name,i)





    #cop[ing new data to old data
    copy_datat_date = datetime.datetime.today()
    copy_datat_date = copy_datat_date.strftime("%Y-%m-%d")

    cpoy_path = r"predicted_data/prediced_data.csv"
    paste_path = r"predicted_data/Old_Prediction//prediced_data_for_("+str(copy_datat_date)+").csv"
    shutil.copy(cpoy_path, paste_path)
    print('the predict file is Copied')
