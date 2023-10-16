from cryptocmd import CmcScraper

# function to download data
def dowbload_dataframe (Stock,Start_Time,End_Time):
    # initialise scraper without time interval
    scraper = CmcScraper(Stock, Start_Time, End_Time)

    # get raw data as list of list
    headers, data = scraper.get_data()

    # get data in a json format
    xrp_json_data = scraper.get_data("json")

    # export the data as csv file, you can also pass optional `name` parameter
    scraper.export("csv", name= Stock, path='Stocks')

    return ('Stocks/'+Stock+'.csv')