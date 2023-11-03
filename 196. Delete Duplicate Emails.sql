# Write your MySQL query statement below
delete
from Person p
where id not in (
    select id from (
        select min(id) as id
        from Person
        group by email
    ) t
)
