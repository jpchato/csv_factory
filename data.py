# importing the module
import pandas as pd 
    
# making data frame from the csv file 
dataframe = pd.read_csv("CrimeData-2021.csv") 
    

dataframe.fillna('No Data', inplace=True)


dataframe['ReportDate'] = pd.to_datetime(dataframe['ReportDate'])
dataframe.sort_values(by='ReportDate', inplace=True)
print(dataframe)

# writing  the dataframe to another csv file
dataframe.to_csv('outputfile.csv', 
                 index = False)
