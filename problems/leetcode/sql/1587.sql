/*
1587. Bank Account Summary II, https://leetcode.com/problems/bank-account-summary-ii/

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account is the primary key for this table.
Each row of this table contains the account number of each user in the bank.
There will be no two users having the same name in the table.

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id is the primary key for this table.
Each row of this table contains all changes made to all accounts.
amount is positive if the user received money and negative if they transferred money.
All accounts start with a balance of 0.
*/

-- 996ms
select
    users.name,
    sum(transactions.amount) as balance
from transactions
inner join users
on transactions.account = users.account
group by transactions.account
having sum(transactions.amount) > 10000;

select
    users.name,
    sum(amount) as balance
from transactions
inner join users
using account
group by account
having sum(amount) > 10000;