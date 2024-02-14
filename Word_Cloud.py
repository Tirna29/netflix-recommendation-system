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

def word_cloud():
    df = get_data_db()
    df['country'] = df['country'].fillna(df['country'].mode()[0])

    df['cast'].replace(np.nan, '', inplace=True)
    df['director'].replace(np.nan, '', inplace=True)

    # Drops

    df.dropna(inplace=True)

    # Drop Duplicates

    df.drop_duplicates(inplace=True)

    from collections import Counter
    genres = list(df['listed_in'])
    list_gen = []

    for gen in genres:
        gen_array = list(gen.split(','))
        for item in gen_array:
            list_gen.append(item.replace(' ', ""))
    gen_dict = Counter(list_gen)

    Linear_Segmented_Color_Map = mc.LinearSegmentedColormap

    color_map = Linear_Segmented_Color_Map.from_list(" ", ['#221f1f', '#b20710', '#f5f5f1'])

    words = ' '.join(list(set(list_gen)))
    plt.rcParams['figure.figsize'] = (8, 8)

    # assigning shape to the word cloud
    my_mask = np.array(Image.open("f1.png"))
    my_wordcloud = WordCloud(max_words=50000000, background_color="white", mask=my_mask, colormap=color_map).generate(
        words)

    plt.imshow(my_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def main():
    word_cloud()

if __name__ == '__main__':
    main()


