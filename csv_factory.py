import pandas as pd

class CSV_Factory():
    
    def csv_reader(csv_file):
        dataframe = pd.read_csv(csv_file) 
        print(dataframe)
        return dataframe
    
    def csv_replace_empty_cells(csv_file):
        dataframe = pd.read_csv(csv_file) 
        dataframe.fillna('No Data', inplace=True)