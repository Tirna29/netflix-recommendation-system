import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def count_plot():
    df = get_data_db()
    df.dropna(inplace=True)

    # Drop Duplicates

    df.drop_duplicates(inplace=True)

    plt.figure(figsize=(11, 9))
    color_list = ['#221f1f', '#b20710', '#e50914']
    plt.xlabel("Ratings")
    plt.ylabel("Total number of shows")
    plt.title("Netflix shows' ratings Histogram")
    sns.countplot(x="rating", data=df, order=df['rating'].value_counts().index[0:200], palette=color_list)
    plt.show()


def main():
    count_plot()


if __name__ == '__main__':
    main()
