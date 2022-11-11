-- Daily Leads and Partners
--/* Write your PL/SQL query statement below */

SELECT TO_CHAR(DATE_ID, 'YYYY-MM-DD') AS DATE_ID,
MAKE_NAME,
COUNT(DISTINCT LEAD_ID) AS UNIQUE_LEADS,
COUNT(DISTINCT PARTNER_ID) AS UNIQUE_PARTNERS
FROM DAILYSALES
GROUP BY
DATE_ID,
MAKE_NAME