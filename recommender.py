import pandas as pd
import pyodbc
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import heapq

def get_data_db():
    server = 'DESKTOP-DB5TLCH\SQLEXPRESS'
    database = 'MyDB'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                SERVER=' + server + ';\
                                DATABASE=' + database + ';\
                                Trusted_Connection=yes;')

    fetch_query = '''select * from dbo.Netflix'''

    return pd.read_sql(fetch_query, connection)

def stem_data(text):
    list1=[]
    stem = PorterStemmer()
    for i in text.split():
        list1.append(stem.stem(i))
    return " ".join(list1)


def get_cast(cast_str):
    cast_array = cast_str.split(",")
    return cast_array[:3]


def split_data(data):
    list1 = data.split(",")
    return list1


def convert_data(data):
    list1 = data.split()
    return list1


def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ", ""))
    return L1


def recommend(movie,new_df,cos_sim):
    index = new_df[new_df['title'] == movie].index[0]
    cosine_vector = cos_sim[index]
    k = 10
    heap = [(-value, index) for index, value in enumerate(cosine_vector)]

    heapq.heapify(heap)

    heapq.heappop(heap)

    while k > 0:
        movie_tuple = heapq.heappop(heap)
        print(new_df.iloc[movie_tuple[1]].title)
        k -= 1

def recommender_system(movie):
    df = get_data_db()

    df = df[['show_id', 'title', 'listed_in', 'description', 'cast', 'director']]

    df = df.fillna("")

    df['cast'] = df['cast'].apply(get_cast)

    df["listed_in"] = df["listed_in"].apply(split_data)
    df["description"] = df["description"].apply(convert_data)
    df["director"] = df["director"].apply(split_data)

    df['cast'] = df['cast'].apply(collapse)
    df['director'] = df['director'].apply(collapse)
    df['description'] = df['description'].apply(collapse)
    df['listed_in'] = df['listed_in'].apply(collapse)

    df["tags"] = df['description'] + df['listed_in'] + df['cast'] + df['director']

    new_df = df.drop(columns=['description', 'director', 'listed_in', 'cast'])

    new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))

    new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())

    new_df["tags"] = new_df["tags"].apply(stem_data)


    counter_vector = CountVectorizer(max_features=5000, stop_words='english')

    vec = counter_vector.fit_transform(new_df['tags']).toarray()

    cos_sim = cosine_similarity(vec)

    recommend(movie,new_df,cos_sim)

def main():
    recommender_system("Chhota Bheem")


if __name__ == '__main__':
    main()
