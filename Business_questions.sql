
/*Question 1: How many reviews do we have per school
SELECT s.school AS 'School', count(*) AS 'Reviews_count'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
GROUP BY s.school;*/

/*Question 2: On average how is rating of each school
SELECT s.school AS 'School',
ROUND(AVG(r.overallScore),2) AS 'AVG_Total_Score',
ROUND(AVG(r.overall),2) AS 'AVG_Overall_Score',
ROUND(AVG(r.curriculum),2) AS 'AVG_Curriculum_Score',
ROUND(AVG(r.jobSupport),2) AS 'AVG_JobSupport_Score'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
GROUP BY s.school
ORDER BY AVG(r.overallScore) DESC;*/

/*Question 3: On average how is rating of each school per year*/
SELECT r.graduatingYear AS 'Year',
s.school AS 'School',
ROUND(AVG(r.overallScore),2) AS 'AVG_Total_Score',
ROUND(AVG(r.overall),2) AS 'AVG_Overall_Score',
ROUND(AVG(r.curriculum),2) AS 'AVG_Curriculum_Score',
ROUND(AVG(r.jobSupport),2) AS 'AVG_JobSupport_Score'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
WHERE r.graduatingYear <> '0' and s.school ='ironhack'
GROUP BY s.school, r.graduatingYear
ORDER BY r.school DESC, r.graduatingYear ASC;


/*Question 4: Courses by year
SELECT r.graduatingYear AS 'Year',
c.courses AS 'Courses',
ROUND(AVG(r.overallScore),2) AS 'AVG_Total_Score',
ROUND(AVG(r.overall),2) AS 'AVG_Overall_Score',
ROUND(AVG(r.curriculum),2) AS 'AVG_Curriculum_Score',
ROUND(AVG(r.jobSupport),2) AS 'AVG_JobSupport_Score'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
INNER JOIN competitive_landscape.courses AS c
	ON c.school = s.school
WHERE r.graduatingYear <> '0' and s.school = 'ironhack'
GROUP BY r.graduatingYear, c.courses 
ORDER BY r.graduatingYear ASC;*/


/*Question 4: location by year
SELECT r.graduatingYear AS 'Year',
l.city_name AS 'City',
ROUND(AVG(r.overallScore),2) AS 'AVG_Total_Score',
ROUND(AVG(r.overall),2) AS 'AVG_Overall_Score',
ROUND(AVG(r.curriculum),2) AS 'AVG_Curriculum_Score',
ROUND(AVG(r.jobSupport),2) AS 'AVG_JobSupport_Score'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
INNER JOIN competitive_landscape.locations AS l
	ON l.school = s.school
WHERE r.graduatingYear <> '0' and s.school = 'ironhack'
GROUP BY r.graduatingYear, l.city_name 
ORDER BY r.graduatingYear ASC;*/

/*Question 5: Jobtittle influences rating by year*/
SELECT r.graduatingYear AS 'Year',
r.jobTitle<>'0' AS 'HAS_JOB',
ROUND(AVG(r.overallScore),2) AS 'AVG_Total_Score',
ROUND(AVG(r.overall),2) AS 'AVG_Overall_Score',
ROUND(AVG(r.curriculum),2) AS 'AVG_Curriculum_Score',
ROUND(AVG(r.jobSupport),2) AS 'AVG_JobSupport_Score'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
WHERE r.graduatingYear <> '0' and s.school = 'ironhack' 
GROUP BY (r.jobTitle<>'0'), r.graduatingYear
ORDER BY r.graduatingYear ASC;





/*
SELECT *
FROM competitive_landscape.courses;

SELECT *
FROM competitive_landscape.badges;

SELECT *
FROM competitive_landscape.locations;

SELECT *
FROM competitive_landscape.reviews AS r;

SELECT *
FROM competitive_landscape.schools;*/
