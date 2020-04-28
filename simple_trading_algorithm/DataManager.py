import pandas as pd



def get_data(max_index):
    df = pd.read_csv('bitmex_api_data/trade_bucketed.csv')[:max_index]
    df['timestamp'] = df['timestamp'].map(pd.to_datetime)
    return df


class DataManager:
    MAX_INDEX = 1000

    def __init__(self):
        self.data = get_data(DataManager.MAX_INDEX)
        self.selected_column = 'low'
        self.start_index = self.get_data_for_index(0)[0]
        self.end_index = self.get_data_for_index(DataManager.MAX_INDEX - 1)[0]

    def get_data_for_index(self, index):
        res_x = self.data.loc[index, 'timestamp']
        res_y = self.data.loc[index, self.selected_column]
        return [res_x, res_y]

    def get_starting_point(self):
        return self.get_data_for_index(0)