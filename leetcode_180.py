##Consecutive Numbers
#/* Write your PL/SQL query statement below */
#
#SELECT DISTINCT A.NUM AS ConsecutiveNums
#FROM
#LOGS A, LOGS B, LOGS C
#WHERE
#A.ID = B.ID -1
#AND B.ID = C.ID -1
#AND A.NUM = B.NUM
#AND B.NUM = C.NUM
