##Customers Who Never Order
#/* Write your PL/SQL query statement below */
#SELECT CUSTOMERS.NAME AS CUSTOMERS FROM CUSTOMERS
#LEFT JOIN ORDERS
#ON ORDERS.CUSTOMERID = CUSTOMERS.ID
#WHERE ORDERS.ID IS NULL