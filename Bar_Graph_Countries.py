import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
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

def bar_graph_countries():
    df = get_data_db()
    df['country'] = df['country'].fillna(df['country'].mode()[0])

    df['cast'].replace(np.nan, '', inplace=True)
    df['director'].replace(np.nan, '', inplace=True)

    # Drops

    df.dropna(inplace=True)

    # Drop Duplicates

    df.drop_duplicates(inplace=True)

    countries = {}

    df['country'] = df['country'].fillna('Unknown')
    country_list = list(df['country'])
    for _, i in enumerate(country_list):
        new_array = list(i.split(','))
        if len(new_array) != 1:
            for j in new_array:
                countries[j] = countries.get(j, 0) + 1
        else:
            countries[i] = countries.get(i, 0) + 1

    sorted_countries = {}
    for country, freq in countries.items():
        country = country.strip()
        sorted_countries[country] = sorted_countries.get(country, 0) + freq

    sorted_countries = {key: val for key, val in
                        sorted(sorted_countries.items(), key=lambda item: item[1], reverse=True)}

    top_countries = {}
    c = 20
    for k, v in sorted_countries.items():
        if c > 0:
            top_countries[k] = v
            c -= 1

    # Set the width and height of the figure
    plt.figure(figsize=(15, 15))

    # Add title
    plt.title("Analysis of top 20 content creating contries")

    color_map = ['#221f1f', '#b20710', '#e50914']

    sns.barplot(y=list(top_countries.keys()), x=list(top_countries.values()), palette=color_map)

    # Add label for vertical axis
    plt.ylabel("Countries")
    plt.xlabel("Number of Shows")
    plt.show()


def main():
    bar_graph_countries()


if __name__ == '__main__':
    main()
