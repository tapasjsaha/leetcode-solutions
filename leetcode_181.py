##Employees Earning More Than Their Managers
#/* Write your PL/SQL query statement below */
#
#SELECT E.NAME AS EMPLOYEE
#FROM
#EMPLOYEE E, EMPLOYEE M
#WHERE
#E.MANAGERID = M.ID
#AND E.SALARY > M.SALARY