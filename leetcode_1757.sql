-- Recyclable and Low Fat Products
--/* Write your PL/SQL query statement below */
SELECT PRODUCT_ID
FROM PRODUCTS
WHERE LOW_FATS = 'Y'
AND RECYCLABLE = 'Y'