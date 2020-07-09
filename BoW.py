from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import mysql.connector
import python_to_sql


def count_words_on_reviews(analyze_school, analyze_year, analyze_word):
    # Connect to SQL database
    cursor, cnx = python_to_sql.connect_to_sql()

    # Get from DB the reviews table
    query = (
    'SELECT * FROM reviews AS r WHERE r.school={} and r.graduatingYear={};'.format('"'+analyze_school+'"',analyze_year))

    cursor.execute(query)

    # Reviews table information to a df
    results = cursor.fetchall()
    reviews_df = pd.DataFrame(results)

    # Get reviews text to a list
    reviews_list = reviews_df[16].to_list()

    # Stopwords
    sw_file = open("stop_words.txt", 'r')
    stop_words = sw_file.read()
    stop_words = stop_words.split('\n')

    # Apply CountVectorizer
    cv = CountVectorizer(reviews_list,stop_words=stop_words)
    count_vector = cv.fit_transform(reviews_list)

    # Get df with words on reviews and their counts
    counts_df = pd.DataFrame(count_vector.toarray(),
                         columns=cv.get_feature_names())

    # Transfer counts_df info to dict_words
    dict_words = {}

    for word in counts_df.columns:
        dict_words[word] = counts_df[word].sum()

    # Get count of analyze_word
    return dict_words[analyze_word]


print(count_words_on_reviews('ironhack',2015,'bad'))
