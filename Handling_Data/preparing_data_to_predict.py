import pandas as pd
from datetime import datetime



#preparing_to_predect agorithm






def preparing_to_predect(DIR,days):
    
    
    #loading downloaded data 
    df_f = pd.read_csv(DIR)
    
    
    #print len of data
    print("✓✓ >>>> Data Has : ",len(df_f) , "   Row")
    
    
    #drop all column exucte date, close.
    #df_f.drop(['Market Cap'], axis=1, inplace=True)
    #df_f.drop(['Date'], axis=1, inplace=True)
    df_f.drop(['Open'], axis=1, inplace=True)
    df_f.drop(['High'], axis=1, inplace=True)
    df_f.drop(['Low'], axis=1, inplace=True)
    df_f.drop(['Volume'], axis=1, inplace=True)
    
    print ('✓✓ >>>> drop all column exucte date, close.')
    
    
    
    #convert column of date to date.
    df_f['Date'] = pd.to_datetime(df_f['Date'], format="%d-%m-%Y")
    
    print ('✓✓ >>>> convert column of date to date.')

    
    
    
    #writting number of day in date.
    for i in range(len(df_f)):
        df_f.Date[i] = df_f.Date[i].strftime('%j')
        
    print ('✓✓ >>>> writting number of day in date.')

        
        
    #convert date to int.
    df_f['Date'] = df_f['Date'].astype(str).astype(int)
    
    print ('✓✓ >>>> convert date to int.')

        
        
    
    #adding Up_Down column.
    df_f['Up_Down'] = 0
    
    print ('✓✓ >>>> adding Up_Down column.')
    
    
    # writting up or down in Up_Down.
    for i in range(len(df_f)-days):
        
        if (((df_f.Close[i+days])/(df_f.Close[i])*100)-100) >= 1 :
            df_f.Up_Down[i] = 1
            
        elif (((df_f.Close[i+days])/(df_f.Close[i])*100)-100) <= 0 :
            df_f.Up_Down[i] = -1
            
        else :
            df_f.Up_Down[i] = 0
            
        
        
#         if df_f.Close[i+ days] > df_f.Close[i] :
#             df_f.Up_Down[i] = 1
            
    print ('✓✓ >>>> writting up or down in Up_Down.')
    
    
    
    # calculate and write the precentaeg of Up_Down.
    df_f['precentaeg'] = 0
    for i in range(days,len(df_f)):
        df_f.precentaeg[i] = int(((df_f.Close[i])/(df_f.Close[i-days])*100)-100)

    print ('✓✓ >>>> calculate and write the precentaeg of Up_Down.')
    
    
    # add last week in data column.
    df_f['befor_1_'] = 0
    df_f['befor_2_'] = 0
    df_f['befor_3_'] = 0
    df_f['befor_4_'] = 0
    df_f['befor_5_'] = 0
    df_f['befor_6_'] = 0
    df_f['befor_7_'] = 0
    df_f['befor_8_'] = 0
    df_f['befor_9_'] = 0
    df_f['befor_10_'] = 0
    df_f['befor_11_'] = 0
    df_f['befor_12_'] = 0
    df_f['befor_13_'] = 0
    df_f['befor_14_'] = 0
    df_f['befor_15_'] = 0
    df_f['befor_16_'] = 0
    df_f['befor_17_'] = 0
    df_f['befor_18_'] = 0
    df_f['befor_19_'] = 0
    df_f['befor_20_'] = 0
    df_f['befor_21_'] = 0
    df_f['befor_22_'] = 0
    df_f['befor_23_'] = 0
    df_f['befor_24_'] = 0
    df_f['befor_25_'] = 0
    df_f['befor_26_'] = 0
    df_f['befor_27_'] = 0
    df_f['befor_28_'] = 0
    df_f['befor_29_'] = 0
    df_f['befor_30_'] = 0


    print ('✓✓ >>>> add last week in data column.')
    
    
    
    
    #writting precentaeg of Up_Down in week data.
    for i in range(30,len(df_f)):
    #    if i in range(14):
    #        continue
        df_f.befor_1_[i] = df_f.precentaeg[i-1]
        df_f.befor_2_[i] = df_f.precentaeg[i-2]
        df_f.befor_3_[i] = df_f.precentaeg[i-3]
        df_f.befor_4_[i] = df_f.precentaeg[i-4]
        df_f.befor_5_[i] = df_f.precentaeg[i-5]
        df_f.befor_6_[i] = df_f.precentaeg[i-6]
        df_f.befor_7_[i] = df_f.precentaeg[i-7]
        df_f.befor_8_[i] = df_f.precentaeg[i-8]
        df_f.befor_9_[i] = df_f.precentaeg[i-9]
        df_f.befor_10_[i] = df_f.precentaeg[i-10]
        df_f.befor_11_[i] = df_f.precentaeg[i-11]
        df_f.befor_12_[i] = df_f.precentaeg[i-12]
        df_f.befor_13_[i] = df_f.precentaeg[i-13]
        df_f.befor_14_[i] = df_f.precentaeg[i-14]
        df_f.befor_15_[i] = df_f.precentaeg[i-15]
        df_f.befor_16_[i] = df_f.precentaeg[i-16]
        df_f.befor_17_[i] = df_f.precentaeg[i-17]
        df_f.befor_18_[i] = df_f.precentaeg[i-18]
        df_f.befor_19_[i] = df_f.precentaeg[i-19]
        df_f.befor_20_[i] = df_f.precentaeg[i-20]
        df_f.befor_21_[i] = df_f.precentaeg[i-21]
        df_f.befor_22_[i] = df_f.precentaeg[i-22]
        df_f.befor_23_[i] = df_f.precentaeg[i-23]
        df_f.befor_24_[i] = df_f.precentaeg[i-24]
        df_f.befor_25_[i] = df_f.precentaeg[i-25]
        df_f.befor_26_[i] = df_f.precentaeg[i-26]
        df_f.befor_27_[i] = df_f.precentaeg[i-27]
        df_f.befor_28_[i] = df_f.precentaeg[i-28]
        df_f.befor_29_[i] = df_f.precentaeg[i-29]
        df_f.befor_30_[i] = df_f.precentaeg[i-30]
        
    print ('✓✓ >>>> writting precentaeg of Up_Down in week data.')
    
    
    
    #drop precentaeg column.
    df_f.drop(['precentaeg'], axis=1, inplace=True)
    
    print ('✓✓ >>>> drop precentaeg column.')    
    
    
    
    #dleating zeros data befor week.
    df_f = df_f[30+days:-days]
    
    print ('✓✓ >>>> dleating zeros data befor week.')
    
    
    print("============= END ",DIR , "=============")    
    
    
    #return data after editing
    return df_f




