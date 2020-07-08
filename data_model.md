Primary table:
    Schools
    Primary Key: schools
    Columns:  'website', 'description', 'LogoUrl', 'school'

Other tables:
    Reviews
    Primary Key: id    #remember to change id to id_review
    Foreign key: schools
    Columns:  'id', 'name', 'anonymous', 'hostProgramName', 'graduatingYear',
       'isAlumni', 'jobTitle', 'tagline', 'body', 'createdAt', 'queryDate',
       'program', 'user', 'overallScore', 'comments', 'overall', 'curriculum',
       'jobSupport', 'review_body', 'school'

    Locations
    Primary Key: id   #remember to change id to id_location
    Foreign key: schools
    Columns:  'id', 'description', 'country.id', 'country.name', 'country.abbrev',
       'city.id', 'city.name', 'city.keyword', 'state.id', 'state.name',
       'state.abbrev', 'state.keyword', 'school'


    Badges
    Primary Key: keyword
    Primary Key: school
    Columns:  'name', 'keyword', 'description', 'school'


    Courses
    Primary Key: courses
    Primary Key: school
    Columns:  'courses', 'school'