/*
    1890. The Latest Login in 2020

    Table: Logins
    +----------------+----------+
    | Column Name    | Type     |
    +----------------+----------+
    | user_id        | int      |
    | time_stamp     | datetime |
    +----------------+----------+
    (user_id, time_stamp) is the primary key for this table.
    Each row contains information about the login time for the user with ID user_id.
*/

-- 634ms
select 
    user_id, 
    max(time_stamp) as last_stamp
from logins
where time_stamp like '2020%'
group by user_id;

-- 1457ms
select 
    user_id, 
    max(time_stamp) as last_stamp
from logins
where year(time_stamp) = 2020
group by user_id;