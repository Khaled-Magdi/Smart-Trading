import pandas as pd
import datetime


from datetime import date
import datetime
import yfinance as yf


def preparing_last_60_day_data(data_name,days):

    #sellecting date range
    Start_calculate = datetime.datetime.today() - datetime.timedelta(days=70)
    Start = Start_calculate.strftime("%Y-%m-%d")
    End_calculate = date.today()
    End = End_calculate.strftime("%Y-%m-%d")

    print ('✓✓ >>>> select date.')



    #downlaoding data
    df_60 = yf.download(data_name+"-USD",Start,End)
    df_60 = df_60.head(-1)

    print ('✓✓ >>>> data daownloaded.')


    #adding row date and drop other culomn _as nuber of day_
    df_60 = df_60.rename(columns = {"Open":"Date"}) 
    df_60['Date'] = (df_60.index).strftime("%j")

    
    df_60.drop(['High'], axis=1, inplace=True)
    df_60.drop(['Low'], axis=1, inplace=True)
    df_60.drop(['Adj Close'], axis=1, inplace=True)
    df_60.drop(['Volume'], axis=1, inplace=True)
    df_60 = df_60.reset_index(drop=True)


    print ('✓✓ >>>> row date is added and drop other culomn.')


    #convert date to int.
    df_60['Date'] = df_60['Date'].astype(str).astype(int)

    print ('✓✓ >>>> convert date to int.')

    
    
#     #adding Up_Down column.
#     df_60['Up_Down'] = 0
    
#     print ('✓✓ >>>> adding Up_Down column.')
    
    
#     # writting up or down in Up_Down.
#     for i in range(len(df_60)-days):
        
#         if (((df_60.Close[i+days])/(df_60.Close[i])*100)-100) >= 1 :
#             df_60.Up_Down[i] = 1
            
#         elif (((df_60.Close[i+days])/(df_60.Close[i])*100)-100) <= 0 :
#             df_60.Up_Down[i] = -1
            
#         else :
#             df_60.Up_Down[i] = 0
            
        
        
    #         if df_f.Close[i+ days] > df_f.Close[i] :
    #             df_f.Up_Down[i] = 1
            
    print ('✓✓ >>>> writting up or down in Up_Down.')
    
    
    
    # calculate and write the precentaeg of Up_Down.
    df_60['precentaeg'] = 0
    for i in range(days,len(df_60)):
        df_60.precentaeg[i] = ((df_60.Close[i])/(df_60.Close[i-days])*100)-100

    print ('✓✓ >>>> calculate and write the precentaeg of Up_Down.')
    
    
    # add last week in data column.
    df_60['befor_1_'] = 0
    df_60['befor_2_'] = 0
    df_60['befor_3_'] = 0
    df_60['befor_4_'] = 0
    df_60['befor_5_'] = 0
    df_60['befor_6_'] = 0
    df_60['befor_7_'] = 0
    df_60['befor_8_'] = 0
    df_60['befor_9_'] = 0
    df_60['befor_10_'] = 0
    df_60['befor_11_'] = 0
    df_60['befor_12_'] = 0
    df_60['befor_13_'] = 0
    df_60['befor_14_'] = 0
    df_60['befor_15_'] = 0
    df_60['befor_16_'] = 0
    df_60['befor_17_'] = 0
    df_60['befor_18_'] = 0
    df_60['befor_19_'] = 0
    df_60['befor_20_'] = 0
    df_60['befor_21_'] = 0
    df_60['befor_22_'] = 0
    df_60['befor_23_'] = 0
    df_60['befor_24_'] = 0
    df_60['befor_25_'] = 0
    df_60['befor_26_'] = 0
    df_60['befor_27_'] = 0
    df_60['befor_28_'] = 0
    df_60['befor_29_'] = 0
    df_60['befor_30_'] = 0


    print ('✓✓ >>>> add last week in data column.')
    
    
    
    
    #writting precentaeg of Up_Down in week data.
    for i in range(30,len(df_60)):
    #    if i in range(14):
    #        continue
        df_60.befor_1_[i] = df_60.precentaeg[i-1]
        df_60.befor_2_[i] = df_60.precentaeg[i-2]
        df_60.befor_3_[i] = df_60.precentaeg[i-3]
        df_60.befor_4_[i] = df_60.precentaeg[i-4]
        df_60.befor_5_[i] = df_60.precentaeg[i-5]
        df_60.befor_6_[i] = df_60.precentaeg[i-6]
        df_60.befor_7_[i] = df_60.precentaeg[i-7]
        df_60.befor_8_[i] = df_60.precentaeg[i-8]
        df_60.befor_9_[i] = df_60.precentaeg[i-9]
        df_60.befor_10_[i] = df_60.precentaeg[i-10]
        df_60.befor_11_[i] = df_60.precentaeg[i-11]
        df_60.befor_12_[i] = df_60.precentaeg[i-12]
        df_60.befor_13_[i] = df_60.precentaeg[i-13]
        df_60.befor_14_[i] = df_60.precentaeg[i-14]
        df_60.befor_15_[i] = df_60.precentaeg[i-15]
        df_60.befor_16_[i] = df_60.precentaeg[i-16]
        df_60.befor_17_[i] = df_60.precentaeg[i-17]
        df_60.befor_18_[i] = df_60.precentaeg[i-18]
        df_60.befor_19_[i] = df_60.precentaeg[i-19]
        df_60.befor_20_[i] = df_60.precentaeg[i-20]
        df_60.befor_21_[i] = df_60.precentaeg[i-21]
        df_60.befor_22_[i] = df_60.precentaeg[i-22]
        df_60.befor_23_[i] = df_60.precentaeg[i-23]
        df_60.befor_24_[i] = df_60.precentaeg[i-24]
        df_60.befor_25_[i] = df_60.precentaeg[i-25]
        df_60.befor_26_[i] = df_60.precentaeg[i-26]
        df_60.befor_27_[i] = df_60.precentaeg[i-27]
        df_60.befor_28_[i] = df_60.precentaeg[i-28]
        df_60.befor_29_[i] = df_60.precentaeg[i-29]
        df_60.befor_30_[i] = df_60.precentaeg[i-30]
        
    print ('✓✓ >>>> writting precentaeg of Up_Down in week data.')
    
    
    
    #drop precentaeg,Close column.
    df_60.drop(['precentaeg'], axis=1, inplace=True)
    df_60.drop(['Close'], axis=1, inplace=True)

    print ('✓✓ >>>> drop precentaeg,Close column.')   
    
    
    
    #get last day.
    df_60 = df_60[-1:]
    
    print ('✓✓ >>>> last day getted.')
    

    return df_60

