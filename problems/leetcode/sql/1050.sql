/*
1050. Actors and Directors Who Cooperated At Least Three Times, 
https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key column for this table.
*/

-- 399ms
select 
    actor_id,
    director_id
from actorDirector
group by 
    actor_id,
    director_id
having count(*) > 2;