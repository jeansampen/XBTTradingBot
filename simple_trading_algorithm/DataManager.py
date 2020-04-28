import pandas as pd

from Enum.PriceType import PriceType


def get_data(max_index):
    df = pd.read_csv('bitmex_api_data/trade_bucketed.csv')[:max_index]
    df['timestamp'] = df['timestamp'].map(pd.to_datetime)
    return df


class DataManager:
    MAX_INDEX = 1000

    def __init__(self):
        self.data = get_data(DataManager.MAX_INDEX)
        self.selected_column = 'low'
        self.start_index = self.get_data_for_index_and_price_type(0, PriceType.LOW)[0]
        self.end_index = self.get_data_for_index_and_price_type(DataManager.MAX_INDEX - 1, PriceType.LOW)[0]

    def get_data_for_index_and_price_type(self, index: int, price_type: PriceType):
        res_x = self.data.loc[index, 'timestamp']
        res_y = self.data.loc[index, price_type.value]
        return [res_x, res_y]

    def get_starting_point_for_price_type(self, price_type):
        return self.get_data_for_index_and_price_type(0, price_type)