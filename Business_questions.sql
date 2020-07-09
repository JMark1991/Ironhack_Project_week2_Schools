
/*Question 1: How many reviews do we have per school*/
SELECT s.school AS 'School', count(*) AS 'Reviews_count'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
GROUP BY s.school;

/*Question 2: On average how is rating of each school*/
SELECT s.school AS 'School',
ROUND(AVG(r.overallScore),2) AS 'AVG_Total_Score',
ROUND(AVG(r.overall),2) AS 'AVG_Overall_Score',
ROUND(AVG(r.curriculum),2) AS 'AVG_Curriculum_Score',
ROUND(AVG(r.jobSupport),2) AS 'AVG_JobSupport_Score'
FROM competitive_landscape.schools AS s
INNER JOIN competitive_landscape.reviews as r
	ON r.school = s.school
GROUP BY s.school
ORDER BY AVG(r.overallScore) DESC;

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
WHERE r.graduatingYear <> '0' 
GROUP BY s.school, r.graduatingYear
ORDER BY r.school DESC, r.graduatingYear ASC;




SELECT *
FROM competitive_landscape.courses;

SELECT *
FROM competitive_landscape.badges;

SELECT *
FROM competitive_landscape.locations;

SELECT *
FROM competitive_landscape.reviews AS r
WHERE r.overall = 0 and overallScore <> 0

SELECT *
FROM competitive_landscape.schools;
