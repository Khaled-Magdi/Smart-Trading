from Handling_Data.downlading_data import dowbload_dataframe
from Handling_Data.preparing_data import prepare_data




# write all stocks to donwloa in for loop
def download_mix_data(Stocks,dayes,start,end):
    for i in range(len(Stocks)):
        data = dowbload_dataframe(Stock=Stocks[i], Start_Time=start, End_Time=end)
        globals() ['df' + str(i)] = prepare_data(data,dayes)

    # mixing all markets in df
    df = df0
    df = df.append([df1, df2, df3, df4])

    # drop close
    df.drop(['Close'], axis=1, inplace=True)

    print('len of all data = ', len(df))
    print(df.head(-20))
    print(len(df))
    
    return df




# function to only mix all data
def mix_data(Stocks,dayes):

    for i in range(len(Stocks)):
        globals() ['df' + str(i)] = prepare_data(Stocks[i],dayes)

    # mixing all markets in df
    df = df0
    df = df.append([df1, df2, df3, df4])

    # drop close
    df.drop(['Close'], axis=1, inplace=True)

    print('len of all data = ', len(df))
    print(df.head(-20))
    print(len(df))
    
    return df
