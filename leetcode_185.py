##Department Top Three Salaries
#/* Write your PL/SQL query statement below */
#SELECT
#DEPARTMENT, EMPLOYEE , SALARY
#FROM
#(SELECT D.NAME AS DEPARTMENT ,E.NAME AS EMPLOYEE,E.SALARY AS SALARY, DENSE_RANK() OVER (PARTITION BY D.NAME ORDER BY SALARY DESC) AS RNK
#FROM EMPLOYEE E, DEPARTMENT D
#WHERE E.DEPARTMENTID = D.ID) TEMP
#WHERE RNK <= 3