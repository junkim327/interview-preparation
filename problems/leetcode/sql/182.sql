/*
182. Duplicate Emails, https://leetcode.com/problems/duplicate-emails/
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
*/

-- 373ms
select email
from person
group by email
having count(*) > 1;

-- 497ms
select distinct p1.email
from person p1
inner join person p2
on p1.email = p2.email
where p1.id != p2.id;