import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MultiLabelBinarizer

import matplotlib.colors as mc

import pyodbc

def get_data_db():
    server = 'DESKTOP-DB5TLCH\SQLEXPRESS'
    database = 'MyDB'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                SERVER=' + server + ';\
                                DATABASE=' + database + ';\
                                Trusted_Connection=yes;')

    fetch_query = '''select * from dbo.Netflix'''

    return pd.read_sql(fetch_query, connection)

def convert_text_to_list(text):
    return text.replace(', ', ',').split(',')




def main():
    df = get_data_db()

    def corr_heat_map():
        df['genres'] = df['listed_in'].apply(convert_text_to_list)

        mb = MultiLabelBinarizer()

        new_df = pd.DataFrame(mb.fit_transform(df['genres']), columns=mb.classes_)

        correlation_matrix = new_df.corr()

        mask = np.zeros_like(correlation_matrix, dtype=bool)
        mask[np.triu_indices_from(mask)] = True

        Linear_Segmented_Color_Map = mc.LinearSegmentedColormap

        color_map = Linear_Segmented_Color_Map.from_list(" ", ['#221f1f', '#b20710', '#f5f5f1'])

        figure, axis = plt.subplots(figsize=(13, 9))

        figure.text(0.4, 0.8, 'Correlation among different Genres', fontsize=16)

        sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, square=True, linewidths=3)

        plt.show()

    corr_heat_map()

if __name__ == '__main__':
    main()