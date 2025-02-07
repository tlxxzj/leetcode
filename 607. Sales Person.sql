# Write your MySQL query statement below
select
    name
from 
    SalesPerson
where
    sales_id not in (
        select 
            distinct(O.sales_id)
        from
            Company C, Orders O
        where 
            C.name = 'RED' and C.com_id = O.com_id
    )