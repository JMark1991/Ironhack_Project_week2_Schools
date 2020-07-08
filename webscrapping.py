# you must populate this dict with the schools required -> try talking to the teaching team about this


schools = {
'ironhack' : 10828,
'app-academy' : 10525,
'springboard' : 11035
}

import re
import pandas as pd
from pandas.io.json import json_normalize
import requests
import mysql.connector
from getpass import getpass

def get_comments_school(school):
  TAG_RE = re.compile(r'<[^>]+>')
  # defines url to make api call to data -> dynamic with school if you want to scrape competition
  url = "https://www.switchup.org/chimera/v1/school-review-list?mainTemplate=school-review-list&path=%2Fbootcamps%2F" + school + "&isDataTarget=false&page=3&perPage=10000&simpleHtml=true&truncationLength=250"
  #makes get request and converts answer to json
  data = requests.get(url).json()
  #converts json to dataframe
  reviews =  pd.DataFrame(data['content']['reviews'])

  #aux function to apply regex and remove tags
  def remove_tags(x):
    return TAG_RE.sub('',x)
  reviews['review_body'] = reviews['body'].apply(remove_tags)
  reviews['school'] = school
  return reviews


def get_school_info(school, school_id):
  url = 'https://www.switchup.org/chimera/v1/bootcamp-data?mainTemplate=bootcamp-data%2Fdescription&path=%2Fbootcamps%2F'+ str(school) + '&isDataTarget=false&bootcampId='+ str(school_id) + '&logoTag=logo&truncationLength=250&readMoreOmission=...&readMoreText=Read%20More&readLessText=Read%20Less'

  data = requests.get(url).json()

  data.keys()

  courses = data['content']['courses']
  courses_df = pd.DataFrame(courses, columns= ['courses'])

  locations = data['content']['locations']
  locations_df = pd.json_normalize(locations)

  badges_df = pd.DataFrame(data['content']['meritBadges'])

  website = data['content']['webaddr']
  description = data['content']['description']
  logoUrl = data['content']['logoUrl']
  school_df = pd.DataFrame([website,description,logoUrl]).T
  school_df.columns =  ['website','description','LogoUrl']

  locations_df['school'] = school
  courses_df['school'] = school
  badges_df['school'] = school
  school_df['school'] = school

  # how could you write a similar block of code to the above in order to record the school ID?

  return locations_df, courses_df, badges_df, school_df

# SQL Python link code
# Table to export table to database
#def table_to_sql(df, cnx, table):
#    df.to_sql(table, cnx, if_exists = 'replace', index = False)


# Create tables if they do not exist on database
#Tables Sql creation code
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

# Connection to SQL database
password = getpass('Please write your localhost root password:\n')
cnx = mysql.connector.connect(user = 'root',password = password, host ='localhost', database = 'competitive_landscape')

# Check if connection is working
if cnx.is_connected():
    print("Connection open")
else:
    print("Connection is not successfully open")


cursor = cnx.cursor()


# Execute all tables to SQL database
cursor.execute(q_schools)
cursor.execute(q_badges)
cursor.execute(q_locations)
cursor.execute(q_reviews)
cursor.execute(q_courses)

# Commits everything to SQL database and closes connections
cnx.commit()
cursor.close()
cnx.close()



reviews_list = []
locations_list = []
courses_list = []
badges_list = []
schools_list = []

for school, id in schools.items():
  print(school)
  a,b,c,d = get_school_info(school,id)
  locations_list.append(a)
  courses_list.append(b)
  badges_list.append(c)
  schools_list.append(d)
  reviews_list.append(get_comments_school(school))


print(
'\n\nLocations: \n', locations_list[0].columns,
'\n\nCourses: \n', courses_list[0].columns,
'\n\nBadges: \n', badges_list[0].columns,
'\n\nSchools: \n', schools_list[0].columns,
'\n\nReviews: \n', reviews_list[0].columns
)





for n in range(3):
    print('NOVA ESCOLAAAAAAAAAAAAAAA')
    print('\n\n')
    print(schools_list[n])
    print('\n\n')
    print(reviews_list[n])
    print('\n\n')
    print(locations_list[n])
    print('\n\n')
    print(badges_list[n])
    print('\n\n')
    print(courses_list[n])
