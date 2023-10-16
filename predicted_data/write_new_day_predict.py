#to writting new day predict in .csv sheat
import datetime
import pandas as pd
from Handling_Data.preparing_last_days import preparing_last_60_day_data




def write_new_day_predict(predict_file_direct,day,data_name,model,index_of_crypto):


    predict_file = pd.read_csv(predict_file_direct)
    
    
    #Update data: 


    #Update date:
    next_day = datetime.datetime.today() + datetime.timedelta(days=day)
    next_day = next_day.strftime("%Y-%m-%d")
    predict_file.Date[day] = next_day



    #preparing data last dayes:
    prepared_data = preparing_last_60_day_data(data_name,day+1)

    #call model:
    # model = data_name+'_predict_RF_' + str(i)+'_day'
    predict = model.predict(prepared_data)


    #write prediction in csv
    predict_file.iloc[day, [index_of_crypto+1]] = predict[0]
    # predict_file.data_name[i] = predict[0]


    predict_file.to_csv("predicted_data/prediced_data.csv",index=False)