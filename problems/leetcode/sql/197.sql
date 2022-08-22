/* 
197 - Rising Temperature, https://leetcode.com/problems/rising-temperature/ 

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the primary key for this table.
This table contains information about the temperature on a certain day.
*/

select w2.id
from weather w1, weather w2
where 
    w2.recordDate = date_add(w1.recordDate, interval 1 day) and
    w2.temperature > w1.temperature;