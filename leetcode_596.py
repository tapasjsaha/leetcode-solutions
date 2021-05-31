-- #Classes More Than 5 Students

/* Write your PL/SQL query statement below */

SELECT CLASS
FROM
(SELECT CLASS, COUNT(DISTINCT STUDENT) AS CNT FROM COURSES GROUP BY CLASS) A
WHERE CNT >= 5

# Not a python problem