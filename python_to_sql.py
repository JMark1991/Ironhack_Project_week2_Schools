import mysql.connector
from getpass import getpass

# SQL Python link code
# Table to export table to database
#def table_to_sql(df, cnx, table):
#    df.to_sql(table, cnx, if_exists = 'replace', index = False)


# Create tables if they do not exist on database
#Tables Sql creation code


def connect_to_sql():
    # Connection to SQL database
    password = getpass('Please write your localhost root password:\n')
    cnx = mysql.connector.connect(user = 'root',password = password, host ='localhost', database = 'competitive_landscape')

    # Check if connection is working
    if cnx.is_connected():
        print("Connection open")
    else:
        print("Connection is not successfully open")

    return cnx.cursor(), cnx

def create_sql_tables(cursor):
    q_schools = ("CREATE TABLE IF NOT EXISTS "
    "schools ("
    "school VARCHAR(100) PRIMARY KEY,"
    "website VARCHAR(100),"
    "description VARCHAR(100),"
    "LogoUrl VARCHAR(100))")

    q_locations = ("CREATE TABLE IF NOT EXISTS "
    "locations ("
    "id INT PRIMARY KEY,"
    "description VARCHAR(500),"
    "country_id INT,"
    "country_name VARCHAR(100),"
    "country_abbrev VARCHAR(100),"
    "city_id INT,"
    "city_name VARCHAR(100),"
    "city_keyword VARCHAR(100),"
    "state_id INT,"
    "state_name VARCHAR(100),"
    "state_abbrev VARCHAR(100),"
    "state_keyword VARCHAR(100),"
    "school VARCHAR(100))")

    q_courses = ("CREATE TABLE IF NOT EXISTS "
    "courses ("
    "courses VARCHAR(100),"
    "school VARCHAR(100),"
    "PRIMARY KEY (courses, school))")

    q_badges = ("CREATE TABLE IF NOT EXISTS "
    "badges ("
    "school VARCHAR(100),"
    "keyword VARCHAR(100),"
    "PRIMARY KEY (school, keyword),"
    "name VARCHAR(100),"
    "description VARCHAR(500))")

    q_reviews = ("CREATE TABLE IF NOT EXISTS "
    "reviews ("
    "id INT PRIMARY KEY,"
    "name VARCHAR(100),"
    "anonymous VARCHAR(100),"
    "hostProgramName VARCHAR(100),"
    "graduatingYear Date,"
    "isAlumni VARCHAR(100),"
    "jobTitle VARCHAR(100),"
    "tagline VARCHAR(100),"
    "body VARCHAR(100),"
    "createdAt Date,"
    "queryDate Date,"
    "program VARCHAR(100),"
    "user VARCHAR(100),"
    "overallScore FLOAT,"
    "comments VARCHAR(100),"
    "overall VARCHAR(100),"
    "curriculum INT,"
    "jobSupport INT,"
    "review_body VARCHAR(100),"
    "school VARCHAR(100))")

    # Execute all tables to SQL database
    cursor.execute(q_schools)
    cursor.execute(q_badges)
    cursor.execute(q_locations)
    cursor.execute(q_reviews)
    cursor.execute(q_courses)

def print_to_sql_tables(cursor,reviews_df,locations_df,courses_df,badges_df,schools_df):
    # Insert rows on tables from dataframes
    # Table Reviews
    q_reviews = ''
    for row in reviews_df:
        q_reviews = "INSERT INTO competitive_landscape.reviews("
        "id,"
        "name,"
        "anonymous,"
        "hostProgramName,"
        "graduatingYear Date,"
        "isAlumni,"
        "jobTitle,"
        "tagline,"
        "body,"
        "createdAt Date,"
        "queryDate Date,"
        "program,"
        "user,"
        "overallScore,"
        "comments,"
        "overall,"
        "curriculum,"
        "jobSupport,"
        "review_body,"
        "school)" + "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(q_reviews, ('XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX','XXX'))
    print()

def commit_sql(cursor, cnx):
    # Commits everything to SQL database and closes connections
    cnx.commit()


def close_sql(cursor,cnx):
    cursor.close()
    cnx.close()
