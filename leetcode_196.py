##Delete Duplicate Emails
##-- This is an oracle solution but it does not work in MySQL.
#DELETE FROM PERSON WHERE ID NOT IN (SELECT MIN(ID) FROM PERSON GROUP BY EMAIL)
#
## This is MySQL solution
#
#DELETE p1 FROM Person p1,
#     Person p2
#WHERE
#     p1.Email=p2.Email AND p1.Id > p2.Id