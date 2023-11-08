# Write your MySQL query statement below
select 'Low Salary' as Category, count(*) as accounts_count
from Accounts 
where income < 20000

union

select 'Average Salary' as Category, count(*) as accounts_count
from Accounts 
where income >=20000 and income <= 50000

union

select 'High Salary' as Category, count(*) as accounts_count
from Accounts 
where income > 50000

