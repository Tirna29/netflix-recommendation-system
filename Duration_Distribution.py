import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc


def convert_text_to_num(text):
    array = text.split()
    return int(array[0])



def get_data_db():
    server = 'DESKTOP-DB5TLCH\SQLEXPRESS'
    database = 'MyDB'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                SERVER=' + server + ';\
                                DATABASE=' + database + ';\
                                Trusted_Connection=yes;')

    fetch_query = '''select * from dbo.Netflix'''

    return pd.read_sql(fetch_query, connection)

def main():
    df = get_data_db()

    movie_df = df[df['type'] == 'Movie']
    new_movie_df = movie_df.dropna(subset=['duration'])

    new_movie_df['duration'] = new_movie_df['duration'].apply(convert_text_to_num)

    sns.kdeplot(data=new_movie_df['duration'], shade=True)
    plt.show()


if __name__ == '__main__':
    main()
